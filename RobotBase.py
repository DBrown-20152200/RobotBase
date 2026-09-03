class RobotBase:
    """A class of robot controls."""

    def __init__(self, name: str, battery_level: Battery, is_moving, sensor_readings):
        """Initialise a robot base
        
        Args:
            _name: Robot name (str)
            _battery_level: Battery charge (float)
            _is_moving: Is robot moving? (bool)
            _sensor_readings: Readings from sensor (dict)
        """
        self._name = name
        self._battery_level = Battery(battery_level)
        self._is_moving = is_moving
        self._sensor_readings = sensor_readings

    @property
    def name(self):
        """Get robot name"""        
        return self._name

    @property
    def is_moving(self):
        """Get robot movement status"""
        return self._is_moving

    @property
    def sensor_readings(self):
        """Get sensor readings dict"""
        return self._sensor_readings

    def move_forward(self, speed):
        """Robot moves forward at set speed.
        
        Args:
            speed: Movement speed (int)
        
        Raises:
            ValueError: If speed is not a positive integer
        """
        if speed <= 0:
            raise ValueError("Speed must be above 0.")
        
        self._is_moving = True

    def stop(self):
        """Robot stops movement."""
        self._is_moving = False;

    def get_sensor_reading(self, name):
        """Get sensor value of specified robot
        
        Args:
            name: Sensor name (str)
        
        Raises:
            ValueError: If name doesn't match self._name

        Returns:
            Measurement from the robot's sensors
        """
        if (name not in self._sensor_readings):
            raise ValueError(f"Sensor - {name} - not found")
        
        return self._sensor_readings[name]

    def set_sensor_reading(self, name, value):
        """Set sensor value of specified robot
        
        Args:
            name: Sensor name (str)
            value: Sensor value (float)
        
        Raises:
            ValueError: Value not float
        """
        if (value < 0):
            raise ValueError("Please enter a number")
        
        self._sensor_readings[name] = str(value) + "cm"

    def report_status(self):
        """Robot status summary
        
        Returns:
            String with all robot data
        """
        return (f"Robot Name: {self._name} | "
                f"Battery Level: {self._battery_level} | "
                f"IsMoving: {self._is_moving} | "
                f"Sensor Readings: {self._sensor_readings}")

    def __str__(self):
        """User-friendly report of the robot's status"""
        return(f"Robot: {self._name}\n"
               f"Battery Level: {self._battery_level}\n"
               f"Is moving: {self._is_moving}\n"
               f"Sensor Readings: {self._sensor_readings}")
    def __repr__(self):
        """Dev-friendly report of all variables"""
        return (f"RobotBase(name = {self._name}\n"
                f"battery_level = {self._battery_level}\n"
                f"is_moving = {self._is_moving}\n"
                f"sensor_readings = {self._sensor_readings})")

class Battery:
    def __init__(self, capacity):
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
    def __init__(self):
        pass

class Sensor:
    def __init__(self):
        pass


if __name__ == "__main__":
    robot = RobotBase("Bingus", 180, False, {"Front":"24cm"})
    android = RobotBase("Sbeve", 270, True, {"Front":"13cm"})

    print(robot)

    print(android)

    print(RobotBase.report_status(robot))
    print(RobotBase.report_status(android))

    RobotBase.set_sensor_reading(robot, "Rear", 47)
    print(RobotBase.get_sensor_reading(robot, "Rear"))

    print(RobotBase.report_status(robot))

