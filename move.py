class Move():
  def __init__(self, fromPos, toPos, special=None):
    self.fromPos = fromPos
    self.toPos = toPos
    self.special = special