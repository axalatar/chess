from pieces import base
from pieces import pieces
import move
import chessboard
import time

class Manager():
  def __init__(self, board=None):
    self.status = "ongoing"
    self.winner = ''
    self.board = board
    self.fake = False
    if(board == None):
      self.board = chessboard.Chessboard()
    self.turn = 1
    # turn % 2 == black, otherwise white turn

  def getBoard(self):
    return self.board

  def setFake(self):
    self.fake = True

  
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

  
  
  def movePiece(self, attemptedMove):
    if(self.status != "ongoing"):
      return
    pieceCoords = attemptedMove.fromPos
    piece = self.board.getPiece(pieceCoords)

    color = piece.getColor()
    if(self.getColorTurn() == color):
      moveSet = piece.getLegalMoves(self) if self.fake == False else piece.getMoves(self)
      destination = attemptedMove.toPos
      if(any((obj.toPos == destination and obj.fromPos == attemptedMove.fromPos and obj.special == attemptedMove.special) for obj in moveSet)):
        self.turn += 1
        self.board.movePiece(attemptedMove)
        type = piece.getType()
        if(type == 'k' or type == 'r'):
          piece.special = True
        if(type == 'p'):
          if(abs(attemptedMove.toPos[1] - attemptedMove.fromPos[1]) == 2):
            piece.special = self.turn
          
        
        if(attemptedMove.special != None):
          
          if(attemptedMove.special == 'en'):
            #on passant            
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
            self.board.setPiece((destination[0], destination[1]), pieces.getPieceByName(attemptedMove.special, color, destination[0], destination[1]))

    
    if(self.fake == False):
      colorTurn = self.getColorTurn()
      enemyColor = 'w' if colorTurn == 'b' else 'b'
      moves = self.getAllMoves(colorTurn)
      if(moves == set()):
        if(self.isInCheck(colorTurn)):
          self.status = "checkmate"
          self.winner = enemyColor
        else:
          self.status = "stalemate"
        
       
         

        
        
    