from project2_Q_learning import *

if __name__ == "__main__":
    # car = Car()
    # car = Car(conn_type="ble", network_uuid='311228c')
    car = Car(conn_type="ble", network_uuid='c1869424')

    instructions = ['go', 'turn right']
    for j in range(0, 4):
        for i in instructions:
            car.execute(i)
            sleep(1)
