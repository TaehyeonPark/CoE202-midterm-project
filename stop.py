from pymodi.modi import *
from time import *
import PID_controller as pid
from utils import *

RIGHT_THRESHOLD = 50
LEFT_THRESHOLD = 50
LEFT_IR_IDX = 0
RIGHT_IR_IDX = 1

BASE_SPEED = 50
OUTPUT_SPEED_THRESHOLD = 40
DELTA_TIME = 0.01
SPEED_LIMIT = 30

MOTER_SPEED = [0, 0]  # L, R

if __name__ == "__main__":
    car = MODI(conn_type="ble", network_uuid='311228c')
    # LEFT_IR = car.irs[LEFT_IR_IDX]
    # RIGHT_IR = car.irs[RIGHT_IR_IDX]
    # print("IR sensor connected")

    MOTER = car.motors[0]
    # print("Moter connected")

    pid_con = pid.PID(dt=DELTA_TIME, Kp=0.5, Kd=0.25, Ki=0)

    # RIGHT(+), LEFT(-)
    MOTER.speed = 0, 0
