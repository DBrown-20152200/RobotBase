class RobotBase:
    """A class of robot controls."""

    def __init__(self, name: str, battery: Battery, motor: Motor, is_running: bool, sensor: Sensor):
        """Initialise a robot base
        
        Args:
            _name: Robot name (str)
            _battery: A robot HAS a battery
            _motor: A robot HAS a motor
            _sensor: A robot HAS a sensor
        """
        self._name = name
        self._battery_level = Battery(battery)
        self._motor = Motor(motor, is_running)
        self._sensor = Sensor(sensor)

    @property
    def name(self):
        """Get robot name"""        
        return self._name
    
    def move(self, distance):
        if self._motor < 0:
            Sensor.read_data()
            Motor.move_forward(distance)
            Battery.drain(15)
        elif self._motor > 0:
            Motor.move_backward(distance)
            Battery.drain(15)
        else:
            Motor.stop()

        if(Sensor.detect_obstacle == True):
            Motor.stop()

    def __str__(self):
        """User-friendly report of the robot's status"""
        return(f"Robot Name: {self.name}, " +
              f"{self._battery_level}, " +
              f"{self._motor}, "
              f"{self._sensor}")
    def __repr__(self):
        """Dev-friendly report of all variables"""
        pass

class Battery:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.level = capacity

    def drain(self, amount):
        """Drain battery level by amount"""
        self.level = max(0, self.level - amount)
        if self.level == 0:
            print("Battery is depleted")

    def charge(self, amount):
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

    def __str__(self):
        """Prints user friendly string"""
        return (f"Motor speed: {self.speed} m/s")

class Sensor:
    def __init__(self, sensor_type: str):
        self.sensor_type = sensor_type
        self.reading = None

        self.sensor_data = self.read_data()
        self.sensor_reading = self.get_reading()

    def read_data(self):
        """Read sensor input"""
        self.sensor_data = f"{self.sensor_type} measurement"
        return self.sensor_data

    def detect_obstacle(self):
        """Has an obstacle been detected"""
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
    robot = RobotBase("Bingus", 180, 24, True, "LIDAR")
    android = RobotBase("Sbeve", 270, 0, False, "Front Camera")

    print(robot)
    # robot.move(52)
    # print(robot)

    print(android)