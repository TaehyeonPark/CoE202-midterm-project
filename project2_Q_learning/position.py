class Position:
  def __init__(self, size):
    self.x = 0
    self.y = 0
    self.max = size

  def action(self, action):
    if action == 'up':
      self._goUp()
    elif action == 'down':
      self._goDown()
    elif action == 'right':
      self._goRight()
    elif action == 'left':
      self._goLeft()

  def _goRight(self):
    if self.max <= self.x:
      return
    self.x = self.x + 1
  
  def _goLeft(self):
    if self.x <= 0:
      return
    self.x = self.x - 1
  
  def _goUp(self):
    if self.y <= 0:
      return
    self.y = self.y - 1
  
  def _goDown(self):
    if self.y >= self.max:
      return
    self.y = self.y + 1