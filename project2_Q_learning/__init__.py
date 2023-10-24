from pymodi.modi import *
from time import *


class Car(MODI):
    def __init__(self, modi_version: int = 1, conn_type: str = "", verbose: bool = False, port=None, network_uuid: str = "", virtual_modules=None):
        super().__init__(modi_version, conn_type, verbose,
                         port, network_uuid, virtual_modules)
        self.MOTOR_FRONT = self.motors[0]
        self.MOTOR_REAR = self.motors[1]

    # Go straight
    def __straight(self, t: float = 1):
        self.MOTOR_FRONT.speed = -100, 100
        self.MOTOR_REAR.speed = 100, -100
        sleep(t)
        self.MOTOR_FRONT.speed = 0, 0
        self.MOTOR_REAR.speed = 0, 0

    # Turn right
    def __right(self, t: float = 0.7):
        self.MOTOR_FRONT.speed = 100, 100
        self.MOTOR_REAR.speed = -100, -100
        sleep(t)
        self.MOTOR_FRONT.speed = 0, 0
        self.MOTOR_REAR.speed = 0, 0

    # Turn left
    def __left(self, t: float = 0.7):
        self.MOTOR_FRONT.speed = -100, -100
        self.MOTOR_REAR.speed = 100, 100
        sleep(t)
        self.MOTOR_FRONT.speed = 0, 0
        self.MOTOR_REAR.speed = 0, 0

    # Executer
    # Expected: ['go', 'go', 'go', 'go', 'go', 'turn right', 'go', 'turn left', 'go', 'turn right', 'go', 'go', 'go', 'turn left', 'go', 'turn right', 'go', 'go', 'go']
    def execute(self, instruction: str):
        if instruction == 'turn right':
            self.__right()
        if instruction == 'turn left':
            self.__left()
        self.__straight()


"""
car = MODI(conn_type="ble", network_uuid='311228c')
car = MODI()
MOTOR_FRONT = car.motors[0]
MOTOR_REAR = car.motors[1]


# Go straight
def __straight(t: float = 1):
    MOTOR_FRONT.speed = -100, 100
    MOTOR_REAR.speed = 100, -100
    sleep(t)
    MOTOR_FRONT.speed = 0, 0
    MOTOR_REAR.speed = 0, 0


# Turn right
def __right(t: float = 0.7):
    MOTOR_FRONT.speed = 100, 100
    MOTOR_REAR.speed = -100, -100
    sleep(t)
    MOTOR_FRONT.speed = 0, 0
    MOTOR_REAR.speed = 0, 0


# Turn left
def __left(t: float = 0.7):
    MOTOR_FRONT.speed = -100, -100
    MOTOR_REAR.speed = 100, 100
    sleep(t)
    MOTOR_FRONT.speed = 0, 0
    MOTOR_REAR.speed = 0, 0


# Executer
# Expected: ['go', 'go', 'go', 'go', 'go', 'turn right', 'go', 'turn left', 'go', 'turn right', 'go', 'go', 'go', 'turn left', 'go', 'turn right', 'go', 'go', 'go']
def execute(instruction: str):
    if instruction == 'turn right':
        __right()
    if instruction == 'turn left':
        __left()
    __straight()
"""
