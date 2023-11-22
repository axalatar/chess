import copy

class Piece():
  def __init__(self, x, y, color):
    self.x = x
    self.y = y
    self.color = color
    self.special = False
#"special" refers to any ability that needs to be remembered between turns, which are whether a king/rook has already moved so we know if it can castle and remembering whether a pawn just moved for an on passant
    self.direction = -1
    if(color == 'b'):
      self.direction = 1


  def isEmpty(self):
    return True if self.color == None else False

  def getType(self):
    return " "
    
  def __str__(self):
    return ' '

  def getColor(self):
    return self.color

  def getDirection(self):
    return self.direction
    
  def getMoves(self, manager):
    return set()
    
  
  def removeIllegalMoves(self, manager, moveList):
    def checkLegal(move):
      manager.movePiece(move, False)
      legal = not manager.isInCheck(self.color)
      manager.undoMove()
      return legal
    
    legalizedMoves = [i for i in moveList if checkLegal(i)]

    return legalizedMoves
          
        
  def getLegalMoves(self, manager):
    return self.removeIllegalMoves(manager, self.getMoves(manager))

  def setPos(self, coords):
    self.x = coords[0]
    self.y = coords[1]

  def getPos(self):
    return (self.x, self.y)