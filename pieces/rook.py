from . import base
import move

def getMovesInDirection(self, manager, deltaX, deltaY):
  legalSpaces = set()
  toX = self.x
  toY = self.y
  for b in range(1, 8):
    toX += deltaX
    toY += deltaY
    if (toX >= 8 or toX < 0):
      break

    if (toY >= 8 or toY < 0):
      break

    piece = manager.board.getPiece((toX, toY))

    if (not piece.isEmpty()):
      if (piece.getColor() != self.getColor()):
        legalSpaces.add(move.Move((self.x, self.y), (toX, toY)))
      break
    legalSpaces.add(move.Move((self.x, self.y), (toX, toY)))
  return legalSpaces

def getAllMoves(self, manager):
  legalSpaces = set()
  legalSpaces.update(getMovesInDirection(self, manager, 0, 1))
  legalSpaces.update(getMovesInDirection(self, manager, 0, -1))
  legalSpaces.update(getMovesInDirection(self, manager, 1, 0))
  legalSpaces.update(getMovesInDirection(self, manager, -1, 0))
  return legalSpaces

class Rook(base.Piece):
  def getType(self):
    return "r"

  def __str__(self):
    return '♖' if self.color == 'w' else '♜'

  def getMoves(self, manager):
    return getAllMoves(self, manager)