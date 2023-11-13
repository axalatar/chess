from . import base
import move

  
def getLegalMoves(self, manager):
  legalSpaces = set()
  for i in range(-1, 2, 2):
    #-1 and 1
    for b in range(-1, 2, 2):
      #another -1 and 1
      toX = self.x
      toY = self.y
      for c in range(8):
        #goes to a max of 8 spaces, just in case something goes wrong, it won't cause an infinite loop
        toX += i
        toY += b

        if (toX >= 8 or toX < 0):
          break
        if (toY >= 8 or toY < 0):
          break

        piece = manager.board.getPiece((toX, toY))
        newMove = move.Move((self.x,self.y),(toX,toY))
        if (piece.isEmpty()):
          legalSpaces.add(newMove)
        elif (piece.getColor() != self.getColor()):
          legalSpaces.add(newMove)
          break
        else:
          break
  return legalSpaces


class Bishop(base.Piece):
  def getType(self):
    return "b"

  def __str__(self):
    return '♗' if self.color == 'w' else '♝'

  def getMoves(self, manager):
    legalSpaces = set()
    legalSpaces.update(getLegalMoves(self, manager))

    return legalSpaces