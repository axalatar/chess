from . import base
from . import rook
from . import bishop



class Queen(base.Piece):
  def getType(self):
    return "q"
    
  def __str__(self):
    return '♕' if self.color == 'w' else '♛'

  def getMoves(self, manager):
    legalSpaces = set()
    legalSpaces.update(rook.getAllMoves(self, manager))
    legalSpaces.update(bishop.getLegalMoves(self, manager))
    return legalSpaces