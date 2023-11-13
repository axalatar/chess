import move

def indexToCoords(x, y):
  return(chr(x+97), 8-y)

def coordsToIndex(x, y):
  return(ord(x)-97, 8-y)
    

class util:
  clear = "\x1b[2J"
  reset_cursor = "\x1b[H"
  red_text = "\x1b[31m"
  reset = "\x1b[0m"
  

class User():

  def __init__(self, manager):
    self.manager = manager
    self.board = manager.getBoard()
    self.error = ""

  def verifyCoordinateInput(self, inputCoords):
    
    if(len(inputCoords) != 2):
      self.error = "Input coordinates must be two characters long"
      return False

    if(not inputCoords[1].isnumeric()):
      self.error = "The second character must be a digit from 1-7"
      return False
    
    coords = coordsToIndex(inputCoords[0], int(inputCoords[1]))
    if(coords[1] < 0 or coords[1] >= 8):
      self.error = "The second character must be a digit from 1-7"
      return False
    
    if(coords[0] < 0 or coords[0] >= 8):
      self.error = "The first character must be a lowercase letter a - h"
      return False


    return coords

  def resetWithMessage(self, message, moves, selected=None):
    print(util.clear + util.reset_cursor)
    self.board.print(moves, selected)
    if(self.manager.status == "ongoing"):
      if(self.manager.isInCheck(self.manager.getColorTurn())):
        turn = "White" if self.manager.getColorTurn() == 'w' else "Black"
        print(util.red_text + turn + " is in check" + util.reset)
    print(message)
  


  def getMove(self):
    while True:
      color = self.manager.getColorTurn()
      if(color == "w"):
        turn = "white"
      else:
        turn = "black"
    
      self.resetWithMessage(self.error, set())
      inputCoords = input("It is " + turn + "'s turn, please enter a move in form of 'a1', 'f3', etc. ")
      coords = self.verifyCoordinateInput(inputCoords)
      if(coords == False):
        continue
      piece = self.board.getPiece(coords)
       


    
      if(piece.getColor() != self.manager.getColorTurn()):
        self.error = "You do not control the chosen piece"
        continue

      moves = piece.getLegalMoves(self.manager)

      self.resetWithMessage("Piece " + inputCoords + " selected", moves, coords)
      inputCoords = input("Select a destination: ")

      destination = self.verifyCoordinateInput(inputCoords)
  
      
      if(destination == False):
        continue

      legal = False
      special = None

      for obj in moves:
        if(obj.toPos == destination):
          legal = True
          if(obj.special != None):
            if(obj.special == 'c' or obj.special == 'en'):
              special = obj.special
            else:
              self.resetWithMessage("What would you like to promote your pawn into?\n 1: Queen\n 2: Bishop\n 3: Knight\n 4: Rook", [], coords)
              num = input()
              if(not num.isnumeric()):
                self.error = "Input must be numeric"
                break
              num = int(num)
              if(num > 4 or num <= 0):
                self.error = "Input must be 1-4"
                break
              match(num):
                case 1:
                  special = 'q'
                case 2:
                  special = 'b'
                case 3:
                  special = 'kn'
                case 4:
                  special = 'r'
              break

      if(legal == False):
        self.error = inputCoords + " is not a valid destination"
        continue

      self.error = ""
      finalMove = move.Move(coords, destination, special)

      return finalMove