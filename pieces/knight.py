import move

from . import base
class Knight(base.Piece):
  def __str__(self):
    return '♘' if self.color == 'w' else '♞'

  def getType(self):
    return "kn"
    
  def getMoves(self, manager):
    legalSpaces = set()

    def calculateLegality(xVar, yVar):
      toX = self.x + xVar
      if(toX >= 8 or toX < 0):
        return
      toY = self.y + yVar
      if(toY >= 8 or toY < 0):
        return
      piece = manager.board.getPiece((toX, toY))
      if(piece.getColor() == self.getColor()):
        return
      newMove = move.Move((self.x, self.y), (toX, toY))
      legalSpaces.add(newMove)
    for i in range(-1, 2, 2):
      #top and bottom, -1 and 1
      for b in range(-1, 2, 2):
        #left and right, again -1 and 1
        calculateLegality(i*2, b)
        calculateLegality(b, i*2)
    return legalSpaces