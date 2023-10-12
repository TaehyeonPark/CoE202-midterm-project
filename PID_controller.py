class PID:
    def __init__(self, dt, Kp=0, Ki=0, Kd=0):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.last_error = 0
        self.delta_time = dt

    def adjust(self, error):
        proportional = self.Kp * error
        integral = self.Ki * error
        derivative = self.Kd * ((error - self.last_error) / (self.delta_time))
        output = proportional + integral + derivative
        self.last_error = error
        return output
