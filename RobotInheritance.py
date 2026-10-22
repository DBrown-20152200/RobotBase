from RobotBase import *

class LineFollower(RobotBase):
    """Robot that moves along a black line"""

    def __init__(self, name: str, battery: Battery, motor: Motor, sensor: Sensor):
        """Initialise line following robot"""
        super().__init__(name, battery, motor, sensor)

    def detect_line(self):
        if self._sensor.reading == "black_line":
            return False
        else:
            return True

    def move(self, distance:float):
        self.detect_line()
        if self.detect_line() == True:
            self._motor.stop()
        else:
            super().move(distance)

class SubRobot(RobotBase):
    """Submarine Robot"""

    def __init__(self, name: str, battery: Battery, motor: Motor, sensor: Sensor):
        """Initialise Submarine Robot"""
        super().__init__(name, battery, motor, sensor)
        self.depth = None

    def change_depth(self, depth):
        if self.depth == None:
            self.depth = depth
        else:
            self.depth += depth

    def propel(self, distance:float, depth:float):
        super().move(distance)
        self.change_depth(depth)
        self._sensor.reading = f"{self.depth}m below sea level"

    
        
if __name__ == "__main__":
    Steve = LineFollower("Steve", Battery(75, 75), Motor(0, False), Sensor("Colour Sensor"))
    print(Steve)

    Steve._sensor.reading = "black_line"
    Steve.move(5)
    print(Steve)

    Steve._sensor.reading = "white_line"
    Steve.move(8)
    print(Steve)

    Yellow = SubRobot("Yellow", Battery(100, 100), Motor(0, False), Sensor("Depth Sensor"))
    print(Yellow)

    Yellow.propel(5, 9)
    print(Yellow)