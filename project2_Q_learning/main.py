from project2_Q_learning import *

if __name__ == "__main__":
    # car = Car(conn_type="ble", network_uuid='311228c')
    # car = Car(conn_type="ble", network_uuid='c1869424')
    car = Car()

    car.exec('go', 1)
    car.exec('turn left', 1)
    car.exec('go', 1)
    car.exec('turn left', 1)
    car.exec('go', 1)
    car.exec('turn right', 1)
    car.exec('go', 1)
    car.exec('turn right', 1)
    car.exec('go', 1)
    car.exec('turn left', 1)
    car.exec('go', 1)
    car.exec('turn left', 1)
    car.exec('go', 1)

    instructions = [('go', 5), ('turn right', 1), ('go', 1), ('turn left', 1), ('go', 1), (
        'turn right', 1), ('go', 3), ('turn left', 1), ('go', 1), ('turn right', 1), ('go', 3)]
    instructions = [('go', 1), ('turn right', 1)]
    for i, m in instructions:
        car.exec(instruction=i, multiplier=m)
    car.stop()
