import manager
import ai
import user

manager = manager.Manager()
user = user.User(manager)




while True:
  move = None
  if(manager.getColorTurn() == 'w'):
    move = user.getMove()
  else:
    move = ai.generateMove(manager)
  manager.movePiece(move)
  user.resetWithMessage("", [], (move.toPos[0], move.toPos[1]))

  match(manager.status):
    case "ongoing":
      pass
    case "stalemate":
      user.resetWithMessage("The game has ended in a stalemate", [])
      break
    case "checkmate":
      color = "White" if manager.winner == 'w' else "Black"
      user.resetWithMessage(color + " has won the game", [])
      break
 
  

  

  



  


  
  
  


# input()

# moves = board.getPiece(coords[0], coords[1]).getLegalMoves(board)
# print(moves)
# board.print(moves)
# printBoard([])



# def findLegalMoves(x, y):
#   piece = getPiece(x, y)
#   legalSpaces = []
#   if piece.color != " ":
#     direction = 1
#     if piece.color == 'w':
#       direction = -1
#   #if it's black it's 1, if it's white it's -1, otherwise it 
#   #can't enter the if statement at all

#     match piece.type:
#       case "p":
#         if y + direction != 8 and y + direction != -1:
#           if getPiece(x, y+direction).color == "e":
#             legalSpaces.append([x, y+direction])
#           #straight forward

#           for i in range(2):
#               b = 1
#               if(i == 1):
#                 b = -1
#               if x+b != 8 and x+b != -1:
#                 piece2 = getPiece(x+b, y+direction)
#                 if piece2.color != "e":
#                   if piece2.color != piece.color:
#                     legalSpaces.append([x+b, y+direction])
#               #diagonals
            
        
#           startPoint = 1
#           if direction == -1:
#             startPoint = 6
#           #where you started from
#           if y == startPoint:
#             if getPiece(x, y+direction*2).color == "e":
#               legalSpaces.append([x, y+(direction*2)])
#         #two forward at start

#   return legalSpaces




# piece = coordsToIndex('a', 2)
# moves = findLegalMoves(piece[0], piece[1])
# for i in moves:
#   print(indexToCoords(i[0], i[1]))
# printBoard(moves)

# turn = "w"

# while(True):
#   pieceCoords = input(util.reset + "Input coordinates of a piece to move: ")
#   pieceIndex = coordsToIndex(pieceCoords[0], int(pieceCoords[1]))
#   piece = getPiece(pieceIndex[0], pieceIndex[1])
#   if(piece.color == "c" or piece.color != turn):
#     print(util.down + "Invalid spot, please choose a piece you control", end="")
#   else:
#     targetCoords = input(util.reset + "Input coordinates of where to move to: ")
#   else:
#     print(util.down + util.clearline + util.up)
#     if(turn == "w"):
#       turn = "b"
#     else:
#       turn = "w"
#   print(util.up + util.up + util.clearline + util.up)
