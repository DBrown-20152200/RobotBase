class RobotBase:
    """A class of robot controls."""

    def __init__(self, name, battery_level, is_moving, sensor_readings):
        """Initialise a robot base
        
        Args:
            _name: Robot name (str)
            _battery_level: Battery charge (float)
            _is_moving: Is robot moving? (bool)
            _sensor_readings: Readings from sensor (dict)
        """
        self._name = name
        self._battery_level = battery_level
        self._is_moving = is_moving
        self._sensor_readings = sensor_readings

    @property
    def name(self):
        """Get robot name"""        
        return self._name

    @property
    def battery_level(self):
        """Get current battery level"""
        return self._battery_level

    @property
    def is_moving(self):
        """Get robot movement status"""
        return self._is_moving

    @property
    def sensor_readings(self):
        """Get sensor readings dict"""
        return self._sensor_readings

    @battery_level.setter
    def battery_level(self, value):
        """Set battery level with validation.
        
        Args: 
            value: New battery level
        
        Raises:
            ValueError: If battery level isn't between 0 and 100
        """
        if (0<=value<=100 == False):
            raise ValueError("Battery level must be 0-100.")
        
        self._battery_level = value

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
            name: Robot name (str)
        
        Raises:
            ValueError: If name doesn't match self._name

        Returns:
            Measurement from the robot's sensors
        """
        if (name != self._name):
            raise ValueError(f"Robot - {name} - not found")
        
        return self._sensor_readings

    def set_sensor_reading(self, name, value):
        """Set sensor value of specified robot
        
        Args:
            name: Robot name (str)
            value: Sensor value (float)
        
        Raises:
            ValueError: Name doesn't match self._name
            ValueError: Value not float
        """
        if (name != self._name):
            raise ValueError(f"Robot - {name} - not found")
        elif (value < 0):
            raise ValueError("Please enter a number")
        
        self._sensor_readings = value

    def __str__(self):
        """User-friendly report of the robot's status"""
        return(f"Robot: {self._name} Battery Level: {self._battery_level:.2f}%\n"
               f"Is moving: {self._is_moving}\n"
               f"Sensor Readings: {self._sensor_readings}")
    def __repr__(self):
        """Dev-friendly report of all variables"""
        return (f"RobotBase(name = {self._name}, "
                f"battery_level = {self._battery_level}, "
                f"is_moving = {self._is_moving}, "
                f"sensor_readings = {self._sensor_readings})")
