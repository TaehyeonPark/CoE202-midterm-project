from pymodi.modi import *
from time import *

IR_THRESHOLD = 20
IR_THRESHOLD_LEFT = 50
IR_THRESHOLD_RIGHT = 50


class Car(MODI):
    def __init__(self, modi_version: int = 1, conn_type: str = "", verbose: bool = False, port=None, network_uuid: str = "", virtual_modules=None):
        super().__init__(modi_version, conn_type, verbose,
                         port, network_uuid, virtual_modules)
        self.IR_LEFT = self.irs[1]
        self.IR_RIGHT = self.irs[0]
        self.MOTOR_FRONT = self.motors[0]
        self.MOTOR_REAR = self.motors[1]

    def stop(self):
        self.MOTOR_FRONT.speed = 0, 0
        self.MOTOR_REAR.speed = 0, 0

    def test_ir(self):
        # print(
        #     f"[LOGGER {time()}] LEFT CROSSED LINE \t LEFT : {self.IR_LEFT.proximity} \t RIGHT : {self.IR_RIGHT.proximity}", end='\r')
        if (self.IR_LEFT.proximity < IR_THRESHOLD_LEFT):
            print('[LOGGER {time()}] \t LEFT')
        if (self.IR_RIGHT.proximity < IR_THRESHOLD_RIGHT):
            print('[LOGGER {time()}] \t RIGHT')

    def until_cross(self):
        print("called def until_cross(self):")
        speed = 35
        speed_front_left, speed_front_right = int(speed*(87/100)), -speed
        speed_rear_left, speed_rear_right = speed, -int(speed*(87/100))

        self.MOTOR_FRONT.speed = speed_front_left, speed_front_right
        self.MOTOR_REAR.speed = speed_rear_left, speed_rear_right

        trigger_left = True
        trigger_right = True

        while trigger_left == True or trigger_right == True:
            LEFT_PROX = self.IR_LEFT.proximity
            RIGHT_PROX = self.IR_RIGHT.proximity
            # print(
            #     f"[LOGGER {time()}] LEFT : {LEFT_PROX} \t RIGHT : {RIGHT_PROX}")
            if (trigger_left == True and LEFT_PROX < IR_THRESHOLD_LEFT and LEFT_PROX > 0):
                trigger_left = False
                self.MOTOR_FRONT.speed = speed_front_left, 0
                self.MOTOR_REAR.speed = speed_rear_left, 0
                print(f"LEFT : {trigger_left} {LEFT_PROX}")
                print(not (trigger_left and trigger_right))

            if (trigger_right == True and RIGHT_PROX < IR_THRESHOLD_RIGHT and RIGHT_PROX > 0):
                trigger_right = False
                self.MOTOR_FRONT.speed = 0, speed_front_right
                self.MOTOR_REAR.speed = 0, speed_rear_right
                print(f"RIGHT : {trigger_right} {RIGHT_PROX}")
                print(not (trigger_left and trigger_right))
            sleep(0.005)
        print("out")

        self.MOTOR_FRONT.speed = 0, 0
        self.MOTOR_REAR.speed = 0, 0

    def after_cross(self, t):
        print("called def after_cross(self):")
        speed = 35
        speed_front_left, speed_front_right = int(speed*(87/100)), -speed
        speed_rear_left, speed_rear_right = speed, -int(speed*(87/100))

        self.MOTOR_FRONT.speed = speed_front_left, speed_front_right
        self.MOTOR_REAR.speed = speed_rear_left, speed_rear_right

        sleep(t)

        self.MOTOR_FRONT.speed = 0, 0
        self.MOTOR_REAR.speed = 0, 0
        print("out")

    # Go straight
    def __straight(self, t: float = 1.3, multiplier: int = 1):
        for i in range(multiplier):
            self.until_cross()
            self.after_cross(t)

    # Turn right
    def __right(self, t: float = 2.6, multiplier: int = 1):
        speed = -45
        speed_front_left, speed_front_right = int(speed*(87/100)), -speed
        speed_rear_left, speed_rear_right = speed, -int(speed*(87/100))

        self.MOTOR_FRONT.speed = speed_front_left, speed_front_right
        self.MOTOR_REAR.speed = speed_rear_left, speed_rear_right

        sleep(0.06)

        self.MOTOR_FRONT.speed = 0, 0
        self.MOTOR_REAR.speed = 0, 0
        speed = 40

        self.MOTOR_FRONT.speed = -int(speed*(90/100)), -speed
        self.MOTOR_REAR.speed = -speed, -int(speed*(90/100))
        sleep(t*multiplier)
        self.MOTOR_FRONT.speed = 0, 0
        self.MOTOR_REAR.speed = 0, 0

    # Turn left
    def __left(self, t: float = 2.35, multiplier: int = 1):
        speed = 40
        self.MOTOR_FRONT.speed = speed, speed
        self.MOTOR_REAR.speed = speed, speed
        sleep(t*multiplier)
        self.MOTOR_FRONT.speed = 0, 0
        self.MOTOR_REAR.speed = 0, 0

    # Executer
    # Expected: ['go', 'go', 'go', 'go', 'go', 'turn right', 'go', 'turn left', 'go', 'turn right', 'go', 'go', 'go', 'turn left', 'go', 'turn right', 'go', 'go', 'go']

    def exec(self, instruction: str, multiplier: int = 1):
        if instruction.lower() == 'turn right':
            self.__right()
        if instruction.lower() == 'turn left':
            self.__left()
        if instruction.lower() == 'go':
            self.__straight(multiplier=multiplier)
