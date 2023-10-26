from pymodi.modi import *
from time import *


class Car(MODI):
    def __init__(self, modi_version: int = 1, conn_type: str = "", verbose: bool = False, port=None, network_uuid: str = "", virtual_modules=None):
        super().__init__(modi_version, conn_type, verbose,
                         port, network_uuid, virtual_modules)
        self.MOTOR_FRONT = self.motors[0]
        self.MOTOR_REAR = self.motors[1]

    # Go straight
    def __straight(self, t: float = 1.78, multiplier: int = 1):
        speed = 50
        self.MOTOR_FRONT.speed = -int(speed*(90/100)), speed
        self.MOTOR_REAR.speed = speed, -int(speed*(90/100))
        sleep(t*multiplier)
        self.MOTOR_FRONT.speed = 0, 0
        self.MOTOR_REAR.speed = 0, 0

    # Turn right
    def __right(self, t: float = .7, multiplier: int = 1):
        speed = 60
        self.MOTOR_FRONT.speed = -int(speed*(90/100)), -speed
        self.MOTOR_REAR.speed = -speed, -int(speed*(90/100))
        sleep(t*multiplier)
        self.MOTOR_FRONT.speed = 0, 0
        self.MOTOR_REAR.speed = 0, 0
        # self.__straight(0.01)

    # Turn left
    def __left(self, t: float = .4, multiplier: int = 1):
        speed = 80
        self.MOTOR_FRONT.speed = speed, speed
        self.MOTOR_REAR.speed = speed, speed
        sleep(t*multiplier)
        self.MOTOR_FRONT.speed = 0, 0
        self.MOTOR_REAR.speed = 0, 0
        # self.__straight(0.025)

    # Executer
    # Expected: ['go', 'go', 'go', 'go', 'go', 'turn right', 'go', 'turn left', 'go', 'turn right', 'go', 'go', 'go', 'turn left', 'go', 'turn right', 'go', 'go', 'go']

    def execute(self, instruction: str):
        if instruction.lower() == 'turn right':
            self.__right()
        if instruction.lower() == 'turn left':
            self.__left()
        if instruction.lower() == 'go':
            self.__straight()
