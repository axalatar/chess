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