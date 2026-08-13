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

        