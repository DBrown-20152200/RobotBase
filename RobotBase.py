class RobotBase:
    """A class of robot controls."""

    def __init__(self, name: str, battery: Battery, motor: Motor, sensor: Sensor):
        """Initialise a robot base
        
        Args:
            _name: Robot name (str)
            _battery: (level: int, capacity: int)
            _motor: (speed: int, is_running: bool)
            _sensor: (sensor_type: str)
        """
        self._name = name
        self._battery = battery
        self._motor = motor
        self._sensor = sensor

    @property
    def name(self):
        """Get robot name"""        
        return self._name
    
    def move(self, distance):
        if self._motor.speed < 0:
            self._sensor.read_data()
            self._motor.move_forward(distance)
            self._battery.drain(2 * distance)
        elif self._motor.speed > 0:
            self._motor.move_backward(distance)
            self._battery.drain(2 * distance)
        else:
            self._motor.stop()

        if(self._sensor.detect_obstacle == True):
            self._motor.stop()

    def __str__(self):
        """User-friendly report of the robot's status"""
        return(f"Robot Name: {self.name}, " +
              f"{self._battery}, " +
              f"{self._motor}, "
              f"{self._sensor}")
    def __repr__(self):
        """Dev-friendly report of all variables"""
        pass

class Battery:
    def __init__(self, level: int, capacity: int):
        self.capacity = capacity
        self.level = level

    def drain(self, amount: int):
        """Drain battery level by amount"""
        self.level = max(0, self.level - amount)
        if self.level == 0:
            print("Battery is depleted")

    def charge(self, amount: int):
        """Charge battery by amount"""
        self.level = min(self.capacity, self.level + amount)
        if self.level == self.capacity:
            print("Battery fully charged")

    def charge_percentage(self):
        """Returns battery level as percentage"""
        return (self.level/self.capacity) * 100

    def __str__(self):
        return (f"Battery charge at {self.charge_percentage():.2f}%")

class Motor:
    def __init__(self, speed: int, is_running: bool):
        self.set_speed(speed)
        if (speed != 0):
            self.is_running = True
        else:
            self.is_running = False

    def move_forward(self, distance:int):
        """Moves the robot forward a set distance"""
        self.distance = distance
        self.is_running = True

    def move_backward(self, distance:int):
        """Moves backward a set distance"""
        self.distance = 0 - distance
        self.is_running = True

    def stop(self):
        """Stops movement"""
        self.distance = 0
        self.is_running = False

    def set_speed(self, speed:int):
        """Set specific robot speed"""
        self.speed = speed
        if (speed == 0):
            self.is_running = False

    def __str__(self):
        """Prints user friendly string"""
        return (f"Motor speed: {self.speed} m/s")

class Sensor:
    def __init__(self, sensor_type: str):
        self.sensor_type = sensor_type
        self.reading = None

        self.sensor_data = self.read_data()
        self.sensor_reading = None

    def read_data(self):
        """Read sensor input"""
        self.sensor_data = f"{self.sensor_type} measurement"
        return self.sensor_data

    def detect_obstacle(self):
        """Returns whether an obstacle has been detected"""
        if self.sensor_data == "obstacle":
            self.obstacle_detected = True
        else:
            self.obstacle_detected = False
        return self.obstacle_detected
        
    def get_reading(self):
        """Return sensor readings"""
        return f"Sensor reading: {self.sensor_data}"

    def __str__(self):
        return (f"Sensor: {self.sensor_type} Reading: {self.sensor_reading}")

    


# Tests RobotBase class if this is the main file
if __name__ == "__main__":
    robot = RobotBase("Bingus", Battery(24,50), Motor(10, True), Sensor("None"))
    print(robot)

    robot._motor.set_speed(34)
    robot.move(5)
    robot._sensor.sensor_type = "Camera"
    print(robot)