from . import pawn
from . import base
from . import knight
from . import bishop
from . import rook
from . import queen
from . import king

def getPieceByName(name, color, x, y):
  match(name):
    case 'p':
      return pawn.Pawn(x, y, color)
    case 'kn':
      return knight.Knight(x, y, color)
    case 'b':
      return bishop.Bishop(x, y, color)
    case 'r':
      return rook.Rook(x, y, color)
    case 'q':
      return queen.Queen(x, y, color)
    case 'k':
      return king.King(x, y, color)
    case _:
      return base.Piece(x, y, color)