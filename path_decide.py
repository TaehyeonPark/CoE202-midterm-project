import json
from position import Position

def setDirection(currDirection, action):
  if currDirection == action:
    return []
  elif currDirection == 'right':
    if action == 'left':
      return ['turn left', 'turn left']
    elif action == 'up':
      return ['turn left']
    elif action == 'down':
      return ['turn right']
  elif currDirection == 'down':
    if action == 'right':
      return ['turn left']
    elif action == 'up':
      return ['turn left', 'turn left']
    elif action == 'left':
      return ['turn right']
  elif currDirection == 'left':
    if action == 'right':
      return ['turn left', 'turn left']
    elif action == 'up':
      return ['turn right']
    elif action == 'down':
      return ['turn left']
  elif currDirection == 'up':
    if action == 'right':
      return ['turn right']
    elif action == 'down':
      return ['turn left', 'turn left']
    elif action == 'left':
      return ['turn left']


class PathDecide:
  def __init__(self, arrayString):
    self.arr = json.loads(arrayString)
    self.currentPosition = Position(size=8)
    
  # startDirection : 'right', 'up', 'down', 'left'
  def getInstructions(self, startDirection):
    result = []
    currentDirection = startDirection
    # 8 by 8 map이라서 7,7이 Goal
    while self.currentPosition.x != 7 or self.currentPosition.y != 7:
      action = self.arr[self.currentPosition.y][self.currentPosition.x]
      turning = setDirection(currentDirection, action)
      result = result + turning + ['go']
      currentDirection = action
      self.currentPosition.action(action)
    return result
    

arrString = """[["right", "right", "right", "right", "right", "down", "down", "down"],
 ["right", "right", "right", "right", "down", "right", "down", "down"],
 ["right", 'down', 'down', 'left', 'right', 'right', 'down', 'down'],
 ['right', 'right', 'right', 'right', 'down', 'left', 'down', 'down'],
 ['right', 'up', 'up', 'left', 'right', 'right', 'right', 'down'],
 ['up', 'left', 'left', 'right', 'up', 'up', 'left', 'down'],
 ['up', 'left', 'left', 'left', 'left', 'left', 'left', 'down'],
 ['up', 'left', 'left', 'left', 'left', 'left', 'left', 'left']]""".replace("'", '"')

decide = PathDecide(arrString)
instruction = decide.getInstructions('right')
print(instruction)