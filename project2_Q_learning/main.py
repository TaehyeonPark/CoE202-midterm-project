from project2_Q_learning import *

if __name__ == "__main__":
    # car = Car(conn_type="ble", network_uuid='311228c')
    # car = Car(conn_type="ble", network_uuid='c1869424')
    car = Car()
    instructions = [('go', 2), ('turn left', 1), ('go', 1), ('turn right', 1), ('go', 1),
                    ('turn left', 1), ('go', 3), ('turn right', 1), ('go', 4), ('turn left', 1), ('go', 3)]
    for i, m in instructions:
        car.exec(instruction=i, multiplier=m)
    car.stop()
