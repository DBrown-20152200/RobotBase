from RobotBase import *

class LineFollower(RobotBase):
    """Robot that moves along a black line"""

    def __init__(self, name: str, battery: Battery, motor: Motor, sensor: Sensor):
        """Initialise a cleaning robot"""
        super().__init__(name, battery, motor, sensor)


    def detect_obstacle(self):
        if self._sensor.reading == "black_line":
            return False
        else:
            return True

if __name__ == "__main__":
    Steve = LineFollower("Steve", Battery(75, 75), Motor(0, False), Sensor("Colour Sensor"))
    print(Steve)

    Steve.move(5)
    print(Steve)

    Steve._sensor.reading = "white_line"
    Steve.move(8)
    print(Steve)