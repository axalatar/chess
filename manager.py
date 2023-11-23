from pieces import base
from pieces import pieces
from pieces import pawn
import move
import chessboard
#import time

class Manager():
  def __init__(self, board=None):
    self.status = "ongoing"
    self.winner = ''
    self.board = board
    self.moves = []
    if(board == None):
      self.board = chessboard.Chessboard()
    self.turn = 1
    # turn % 2 == black, otherwise white turn



    

  def getBoard(self):
    return self.board    

  
  def getPieces(self, color):
    pieceCoords = self.board.getWhitePieces() if color == 'w' else self.board.getBlackPieces()
    pieces = set()
    for piece in pieceCoords:
      pieces.add(self.board.getPiece(piece))
    return pieces


  def getAllMoves(self, color, legal=True):
    pieces = self.getPieces(color)
    moves = set()
      
    for piece in pieces:
      newMoves = piece.getLegalMoves(self) if legal == True else piece.getMoves(self)
      moves.update(newMoves)

    return moves

  def getTurn(self):
    return self.turn

  def getColorTurn(self):
    return 'b' if self.turn % 2 == 0 else 'w'


  def findAttackingPiece(self, pieceCoords, color, ignoreKings=False):
    enemyColor = 'w' if color == 'b' else 'b'
    pieces = self.getPieces(enemyColor)
    for piece in pieces:
      if(ignoreKings==True):
        if(piece.getType()=="k"):
          if(piece.special==False):
            continue
      moves = piece.getMoves(self)
      if(any(obj.toPos == pieceCoords for obj in moves)):
        return True
    return False

  def isInCheck(self, color):
    kingCoords = self.board.getKing(color)
    
    if(self.findAttackingPiece(kingCoords, color, True)):
      return True
    return False

  
  def undoMove(self):
    if(self.turn == 1):
      return
    self.turn -= 1
    lastMove = self.moves.pop()
    backwardMove = move.Move(lastMove.toPos, lastMove.fromPos, lastMove.captured, lastMove.special)
    self.board.movePiece(backwardMove)
    if(lastMove.captured is not None):
      self.board.setPiece(lastMove.captured.getPos(), lastMove.captured)
      # this will also work with en passant!
      
    piece = self.board.getPiece(lastMove.fromPos)
    if(piece.getType() == 'k' or piece.getType() == 'r'):
      if(piece.special == self.turn):
        piece.special = False
    if(piece.getType() == 'p'):
      if(piece.special == self.turn):
        piece.special = False



    if(lastMove.special is not None):
      if(lastMove.special == 'c'):
        #castle
        Y = lastMove.toPos[1]
        if(lastMove.toPos[0] == 2):
          self.board.movePiece(move.Move((3, Y), (0, Y)))
        else:
          self.board.movePiece(move.Move((5, Y), (7, Y)))
      else:
        #promotion
        self.board.setPiece(lastMove.fromPos, lastMove.captured)
    
    if(self.status != "ongoing"):
      self.status = "ongoing"
      self.winner = ''
    
    
  def checkMate(self, moves=None):
    # check if there is a checkmate or stalemate on the board, you can optionally pass in a list
    # of moves if they've already been found
    colorTurn = self.getColorTurn()
    enemyColor = 'w' if colorTurn == 'b' else 'b'
    moves = self.getAllMoves(colorTurn) if moves is None else moves
    if(moves == set()):
      if(self.isInCheck(colorTurn)):
        self.status = "checkmate"
        self.winner = enemyColor
      else:
        self.status = "stalemate"

  def movePieceTrusted(self, attemptedMove):
    #this is for when we know the move is legal and don't want to check it again

    destination = attemptedMove.toPos
    piece = self.board.getPiece(attemptedMove.fromPos)
    if(self.board.getPiece(destination).getType() != " "):
      attemptedMove.captured = self.board.getPiece(destination)
      print(attemptedMove.captured)
    self.turn += 1
    self.board.movePiece(attemptedMove)
    type = piece.getType()
    if(type == 'k' or type == 'r'):
      if(piece.special == False):
        piece.special = self.turn
        # otherwise, there is no way to know whether or not a king/rook has moved for the first
        # time while undoing a move, which is necessary for castling          
          

    if(type == 'p'):
      if(abs(attemptedMove.toPos[1] - attemptedMove.fromPos[1]) == 2):
        piece.special = self.turn
        # this is for en passant, as you can only do it the turn after the two square move
        
    if(attemptedMove.special is not None):
        
      if(attemptedMove.special == 'en'):
        #on passant  
        attemptedMove.captured = self.board.getPiece((destination[0], destination[1] + (piece.getDirection()*-1)))          
        self.board.setPiece((destination[0], destination[1] + (piece.getDirection()*-1)), base.Piece(destination[0], destination[1] + (piece.getDirection()*-1), None))
      elif(attemptedMove.special == 'c'):
        #castle
        Y = destination[1]
        if(destination[0] == 2):
          self.board.movePiece(move.Move((0, Y), (3, Y)))
        else:
          self.board.movePiece(move.Move((7, Y), (5, Y)))
      else:
        #promotion
        attemptedMove.captured = self.board.getPiece(destination)
        self.board.setPiece((destination[0], destination[1]), pieces.getPieceByName(attemptedMove.special, color, destination[0], destination[1]))
    self.moves.append(attemptedMove)


  def movePiece(self, attemptedMove):
    if(self.status != "ongoing"):
      return
    pieceCoords = attemptedMove.fromPos
    piece = self.board.getPiece(pieceCoords)

    color = piece.getColor()
    if(self.getColorTurn() == color):
      moveSet = piece.getLegalMoves(self)
      destination = attemptedMove.toPos
      if(any((obj.toPos == destination and obj.fromPos == attemptedMove.fromPos and obj.special == attemptedMove.special) for obj in moveSet)):
        self.movePieceTrusted(attemptedMove)
        self.checkMate()
        return