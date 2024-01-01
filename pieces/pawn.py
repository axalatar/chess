from . import base
import move

class Pawn(base.Piece):

  def getType(self):
    return "p"
    
  def __str__(self):
    return '♙' if self.color == 'w' else '♟'
    
  def getMoves(self, manager):
    legalSpaces = set()

    def addLegalMove(coords):
      f = (self.x, self.y)
      t = coords
      #f = from, t = to
      Y = t[1]
      if(Y == 0 or Y == 7):
        legalSpaces.add(move.Move(f, t, 'kn'))
        legalSpaces.add(move.Move(f, t, 'q'))
        legalSpaces.add(move.Move(f, t, 'r'))
        legalSpaces.add(move.Move(f, t, 'b'))
        #i shouldve written a function for this but im lazy
        #this is for promotion
      else:
        legalSpaces.add(move.Move(f, t))
        
    x = self.x
    y = self.y
    if y + self.direction != 8 and y + self.direction != -1:

      #straight forward
      if manager.board.getPiece((x, y+self.direction)).isEmpty():
        addLegalMove((x, y+self.direction))
        
      #diagonals
      for i in [-1, 1]:
          if x+i != 8 and x+i != -1:
            piece2 = manager.board.getPiece((x+i, y+self.direction))
            if not piece2.isEmpty():
              if piece2.color != self.color:
               addLegalMove((x+i, y+self.direction))
            else:
              #en passant
              piece3 = manager.board.getPiece((x+i, y))
              if piece3.getType() == 'p' and piece3.color != self.color:
                if(piece3.special == manager.turn):
                  legalSpaces.add(move.Move((self.x, self.y), (x+i, y+self.direction), "en"))

      
      #two forward at start
      startPoint = 6 if self.direction == -1 else 1
      if y == startPoint:
        if manager.board.getPiece((x, y+(self.direction*2))).isEmpty() and manager.board.getPiece((x, y+self.direction)).isEmpty():
          addLegalMove((x, y+(self.direction*2)))

    return legalSpaces