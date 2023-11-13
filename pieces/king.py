from . import base
import move

class King(base.Piece):
  def __str__(self):
    return '♔' if self.color == 'w' else '♚'

  def getType(self):
    return "k"

  def getMoves(self, manager):
    legalSpaces = set()
    for i in range(-1, 2):
      for b in range(-1, 2):
        toX = self.x + i
        toY = self.y + b

        if(toX >= 8 or toX < 0):
          continue

        if(toY >= 8 or toY < 0):
          continue

        piece = manager.board.getPiece((toX, toY))
        if(piece.getColor() == self.getColor()):
          continue
          
        legalSpaces.add(move.Move((self.x, self.y), (self.x + i, self.y + b)))

    if(self.special == False):
      if(not manager.isInCheck(self.color)):
        for rooks in [(7, 5, -1), (0, 3, 1)]:
          rook = manager.board.getPiece((rooks[0], self.y))
          if(rook.getType() == 'r' and rook.special == False):
            empty = True
            for i in range(rooks[0]+rooks[2], rooks[1]+rooks[2], rooks[2]):
              if(manager.board.getPiece((i, self.y)).getType() != ' '):
                empty = False
                break
            if(empty == True):
              if(manager.findAttackingPiece((self.x+(rooks[2]*-1), self.y), self.color) == False):
                castleMove = move.Move((self.x, self.y), (self.x+(rooks[2]*-2), self.y), "c")
              
                legalSpaces.add(castleMove)
  
    return legalSpaces