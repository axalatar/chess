import copy



def pieceValue(type):
  match(type):
      case "p":
        return 10
      case "kn":
        return 30
      case "b":
        return 35
      case "r":
        return 50
      case "q":
        return 90
      case "k":
        return 1000

def evaluateBoard(manager, color):
  value = 0
  pieces = set()
  pieces.update(manager.board.getWhitePieces())
  pieces.update(manager.board.getBlackPieces())
  
  for pieceCoords in pieces:
    piece = manager.board.getPiece(pieceCoords)
    tempValue = pieceValue(piece.getType())
    
    value += (tempValue if piece.color == color else (tempValue * -1))
  return value
  
  
  
  

def generateMove(manager):
  moves = manager.getAllMoves(manager.getColorTurn())
  bestValue = [-10000]
  for move in moves:
    managerClone = copy.deepcopy(manager)
    managerClone.movePiece(move)
    value = evaluateBoard(managerClone, manager.getColorTurn()) 
    if(value > bestValue[0]):
      bestValue = [value, move]
  return bestValue[1]
  