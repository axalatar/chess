from pieces import pieces
from pieces import base


class util:
  blue = "\x1b[44m"
  black = "\x1b[107m"
  red_background = "\x1b[41m"
  yellow_background = "\x1b[43m"

  reset = "\x1b[0m"
  clearline = "\u001b[2K"
  down = "\u001b[1B"
  up = "\u001b[1A"


#easily use escape codes

pieceData = {
  " ": [None, None],
  "♙": ["p", "w"],
  "♟": ["p", "b"],
  "♖": ["r", "w"],
  "♜": ["r", "b"],
  "♘": ["kn", "w"],
  "♞": ["kn", "b"],
  "♗": ["b", "w"],
  "♝": ["b", "b"],
  "♕": ["q", "w"],
  "♛": ["q", "b"],
  "♔": ["k", "w"],
  "♚": ["k", "b"],
}
#assign meaning to the ascii pieces


class Chessboard:

  def getBoard(self):
    return self.board

  def getKing(self, color):
    if (color == 'w'):
      return self.whiteKing
    else:
      return self.blackKing

  def getPiece(self, coords):
    return self.board[coords[1]][coords[0]]

  def setPiece(self, coords, piece):
    color = piece.getColor()
    self.whitePieces.discard(coords)
    self.blackPieces.discard(coords)
    self.board[coords[1]][coords[0]] = piece
    if (piece.getType() == 'k'):
      if (color == 'w'):
        self.whiteKing = coords
      else:
        self.blackKing = coords
    if (color == 'w'):
      self.whitePieces.add(coords)
    elif (color == 'b'):
      self.blackPieces.add(coords)

  def movePiece(self, move):
    fromPos = move.fromPos
    toPos = move.toPos
    piece = self.getPiece(fromPos)
    self.setPiece(toPos, piece)
    self.setPiece(fromPos, base.Piece(fromPos[0], fromPos[1], None))
    piece.setPos(toPos)

  def getBlackPieces(self):
    return self.blackPieces

  def getWhitePieces(self):
    return self.whitePieces

  def __init__(self, board=None):
    self.whitePieces = set()
    self.blackPieces = set()
    self.board = [["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
                  ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
                  [" ", " ", " ", " ", " ", " ", " ", " "],
                  [" ", " ", " ", " ", " ", " ", " ", " "],
                  [" ", " ", " ", " ", " ", " ", " ", " "],
                  [" ", " ", " ", " ", " ", " ", " ", " "],
                  ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
                  ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]]

    if (board != None):
      self.board = board
      #if you want a custom board for some reason, really just for testing
    
    for x in range(len(self.board)):
      for y in range(len(self.board[x])):
        data = pieceData[self.getPiece((x, y))]
        self.setPiece((x, y), pieces.getPieceByName(data[0], data[1], x, y))
        if (data[1] == 'w'):
          self.whitePieces.add((x, y))
        elif (data[1] == 'b'):
          self.blackPieces.add((x, y))
#convert them into piece objects


  
  def print(self, moves, selected=None):
    color = util.black

    def switchColor(color):
      return util.black if color == util.blue else util.blue

    print(" a b c d e f g h")
    #coordinates on the top
    for x in range(len(self.board)):
      print(util.reset + str(8 - x), end="")
      #coordinates on the left
      color = switchColor(color)
      for y in range(len(self.board[x])):
        special = ""

        for move in moves:
          toPos = move.toPos
          fromPos = move.fromPos
          if y == toPos[0] and x == toPos[1]:
            special = util.red_background

          if (fromPos[0] == y and fromPos[1] == x):
            special = util.yellow_background
        if (selected != None and selected[0] == y and selected[1] == x):
          special = util.yellow_background
          #if there are no legal moves, you still
          #want to know which piece was selected

        # if((y, x) in self.blackPieces):
        #   special = "\033[0;43m" # black orange back, white green back
        # elif((y, x) in self.whitePieces):
        #   special = "\033[0;42m"

        print(color + special + str(self.board[x][y]), end=" ")
        #end=" " makes it so there is a space instead of \n

        color = switchColor(color)
        #colored tiles!

      print(util.reset)
      #this makes a new line at end of the row
    print()
