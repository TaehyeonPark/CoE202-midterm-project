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
    return self._merge_and_count(result)
  
  def _merge_and_count(self, input_list):
    result = []
    current_element = input_list[0]
    count = 1

    for i in range(1, len(input_list)):
        if input_list[i] == current_element:
            count += 1
        else:
            result.append((current_element, count))
            current_element = input_list[i]
            count = 1

    result.append((current_element, count))

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
instruction = decide.getInstructions('right') # 첫 방향 설정 필요
print(instruction)
# Expected: ['go', 'go', 'go', 'go', 'go', 'turn right', 'go', 'turn left', 'go', 'turn right', 'go', 'go', 'go', 'turn left', 'go', 'turn right', 'go', 'go', 'go']
# Expected: [('go', 5), ('turn right', 1), ('go', 1), ('turn left', 1), ('go', 1), ('turn right', 1), ('go', 3), ('turn left', 1), ('go', 1), ('turn right', 1), ('go', 3)]