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
                speed: Movement speed
            
            Raises:
                ValueError: If speed is not a positive integer
            """
            if speed <= 0:
                raise ValueError("Speed must be above 0.")
            self._is_moving = True

        