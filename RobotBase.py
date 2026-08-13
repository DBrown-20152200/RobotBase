class RobotBase:
    """A class of robot controls."""

    def __init__(self):
        """Initialise a robot base
        
        Args:
            _name: Robot name (str)
            _battery_level: Battery charge (float)
            _is_moving: Is robot moving? (bool)
            _sensor_readings: Readings from sensor (dict)
        """