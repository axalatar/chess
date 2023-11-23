import manager
import time
import user
manager = manager.Manager()
tempUser = user.User(manager)


nodes = 0
captures = 0
ep = 0
castles = 0
promotions = 0
checks = 0
checkmates = 0

def perft(depth, manager):
  global nodes
  global captures
  global ep
  global castles
  global promotions
  global checks
  global checkmates

  if(depth == 0):
    nodes += 1
    return
  
  moves = manager.getAllMoves(manager.getColorTurn(), False)
  color = manager.getColorTurn()
  for move in moves:
    manager.movePieceTrusted(move)
    if(manager.isInCheck(color)): #if the move puts the player in check, it is illegal
      manager.undoMove()
      continue

    if(move.special == 'c'): 
      castles += 1
    elif(move.special == 'en'):
      ep += 1
    elif(move.special is not None):
      promotions += 1
    if(manager.isInCheck(manager.getColorTurn())):
      checks += 1
      manager.checkMate()
      if(manager.status == "checkmate"):
        checkmates += 1
    if(move.captured is not None):
      captures += 1

    perft(depth-1, manager)
    manager.undoMove()



if(__name__ == "__main__"):
  DEPTH = 4

  start = time.time()
  perft(DEPTH, manager)
  end = time.time()
  print("Time elapsed: " + str(end - start) + " seconds")
  print(f"""
      Nodes: {nodes}
      Captures: {captures}
      En Passant: {ep}
      Castles: {castles}
      Promotions: {promotions}
      Checks: {checks}
      Checkmates: {checkmates}""")