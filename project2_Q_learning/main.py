from project2_Q_learning import *

if __name__ == "__main__":
    # car = Car()
    # car = Car(conn_type="ble", network_uuid='311228c')
    car = Car(conn_type="ble", network_uuid='c1869424')

    instructions = [('go', 5), ('turn right', 1), ('go', 1), ('turn left', 1), ('go', 1), (
        'turn right', 1), ('go', 3), ('turn left', 1), ('go', 1), ('turn right', 1), ('go', 3)]
    # car.execute(instruction='go', multiplier=3)
    for x in instructions:
        car.execute(instruction=x[0], multiplier=x[1])
