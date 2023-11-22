class Move():
  def __init__(self, fromPos, toPos, captured=None, special=None):
    self.fromPos = fromPos
    self.toPos = toPos
    self.special = special
    self.captured = captured