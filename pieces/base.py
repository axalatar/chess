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
    newList = copy.deepcopy(moveList)
    color = self.getColor()
    enemyColor = 'w' if color == 'b' else 'b'
    for move in moveList:
      simManager = copy.deepcopy(manager)
      simManager.setFake()
      simBoard = simManager.getBoard()
      simManager.movePiece(move)
      allMoves = simManager.getAllMoves(enemyColor, False)


      for enemyMove in allMoves:    
        if(simBoard.getKing(color) == enemyMove.toPos):
          
          for otherMove in newList:
            if(otherMove.toPos == move.toPos):
              
              newList.remove(otherMove)
              break
          break

    return newList
          
        
  def getLegalMoves(self, manager):
    return self.removeIllegalMoves(manager, self.getMoves(manager))

  def setPos(self, coords):
    self.x = coords[0]
    self.y = coords[1]

  def getPos(self):
    return (self.x, self.y)