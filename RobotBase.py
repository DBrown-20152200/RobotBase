class RobotBase:
    """A class of robot controls."""

    def __init__(self, name: str, battery: Battery, motor: Motor, sensor: Sensor):
        """Initialise a robot base
        
        Args:
            _name: Robot name (str)
            _battery: A robot HAS a battery
            _motor: A robot HAS a motor
            _sensor_readings: Readings from sensor (dict)
        """
        self._name = name
        self._battery_level = Battery(battery)
        self._motor = Motor(motor)
        self._sensor = Sensor(sensor)

    @property
    def name(self):
        """Get robot name"""        
        return self._name

    def move(self, distance):
        if self.speed < 0:
            Motor.move_forward(distance)
            Battery.drain(15)            
        elif self.speed > 0:
            Motor.move_backward(distance)
            Battery.drain(15)
        else:
            self.stop()

    # def get_sensor_reading(self, name):
    #     """Get sensor value of specified robot
        
    #     Args:
    #         name: Sensor name (str)
        
    #     Raises:
    #         ValueError: If name doesn't match self._name

    #     Returns:
    #         Measurement from the robot's sensors
    #     """
    #     if (name not in self._sensor_readings):
    #         raise ValueError(f"Sensor - {name} - not found")
        
    #     return self._sensor_readings[name]

    # def set_sensor_reading(self, name, value):
    #     """Set sensor value of specified robot
        
    #     Args:
    #         name: Sensor name (str)
    #         value: Sensor value (float)
        
    #     Raises:
    #         ValueError: Value not float
    #     """
    #     if (value < 0):
    #         raise ValueError("Please enter a number")
        
    #     self._sensor_readings[name] = str(value) + "cm"

    def report_status(self):
        """Robot status summary
        
        Returns:
            String with all robot data
        """
        pass

    def __str__(self):
        """User-friendly report of the robot's status"""
        return(f"Robot Name: {self.name} " +
              f"Battery: {self._battery_level}" +
              f"Motor: {self._motor}")
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
        return (f"Battery charge at {self.charge_percentage():.2f}% ")

class Motor:
    def __init__(self, speed: int):
        self.speed = speed
        if (speed != 0):
            self.is_running = True
        else:
            self.is_running = False

    def move_forward(self, distance:int):
        """Moves the forward a set distance"""
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

    def read_data(self):
        """Read sensor input"""
        pass

    def detect_obstacle(self):
        """Has an obstacle been detected"""
        pass

    def get_reading(self):
        """Return sensor readings"""
        pass


# Tests RobotBase class if this is the main file
if __name__ == "__main__":
    robot = RobotBase("Bingus", 180, 24, {"Front":"24cm"})
    android = RobotBase("Sbeve", 270, 0, {"Front":"13cm"})

    print(robot)

    print(android)

    # print(RobotBase.report_status(robot))
    # print(RobotBase.report_status(android))

    # RobotBase.set_sensor_reading(robot, "Rear", 47)
    # print(RobotBase.get_sensor_reading(robot, "Rear"))

    # print(RobotBase.report_status(robot))

