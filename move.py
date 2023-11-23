class Move():
  def __init__(self, fromPos, toPos, special=None, captured=None):
    self.fromPos = fromPos
    self.toPos = toPos
    self.special = special
    self.captured = captured