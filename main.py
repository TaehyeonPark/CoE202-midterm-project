from pymodi.modi import *
from time import *
import PID_controller as pid
from utils import *

RIGHT_THRESHOLD = 50
LEFT_THRESHOLD = 50
LEFT_IR_IDX = 0
RIGHT_IR_IDX = 1
LEFT_MOTER_IDX = 1
RIGHT_MOTER_IDX = 0
LEFT_MOTER_IDX_2 = 2
RIGHT_MOTER_IDX_2 = 3
BASE_SPEED = 50
LEFT_DEFAULT_SPEED = 80
RIGHT_DEFAULT_SPEED = 100

OUTPUT_SPEED_THRESHOLD = 40
DELTA_TIME = 0.001
SPEED_LIMIT = 30

if __name__ == "__main__":
    car = MODI(conn_type="ble", network_uuid='311228c')
    LEFT_IR = car.irs[LEFT_IR_IDX]
    RIGHT_IR = car.irs[RIGHT_IR_IDX]
    MOTER = car.motors[0]

    pid_con = pid.PID(dt=DELTA_TIME, Kp=0.1, Kd=0.015, Ki=0)
    MOTER.speed = 0, 0

    while True:
        error = (LEFT_IR.proximity - RIGHT_IR.proximity)
        output = mapper(pid_con.adjust(error=error))
        sleep(DELTA_TIME)
        # front
        RIGHT_MOTER_SPEED = BASE_SPEED + output * SPEED_LIMIT
        LEFT_MOTER_SPEED = (BASE_SPEED - output * SPEED_LIMIT)

        print(
            f"[LOGGER {time()}]\t OUPUT : {output}| \tLEFT : {LEFT_MOTER_SPEED}\tRIGHT : {RIGHT_MOTER_SPEED}", end='\r')

        # RIGHT(+), LEFT(-)
        MOTER.speed = (LEFT_MOTER_SPEED * 0.9), -RIGHT_MOTER_SPEED
