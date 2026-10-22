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

    def __init__(self, name: str, battery: Battery, motor: Motor, sensor: Sensor, depth: float):
        """Initialise Submarine Robot"""
        super().__init__(name, battery, motor, sensor)
        self._depth = depth
        self._sensor.reading = f"{self._depth}m below sea level"


    def change_depth(self, depth):
        if self._depth == None:
            self._depth = depth
        elif(self._depth + depth > 0):
            self._depth += depth
        else:
            self._depth = 0
        self._battery.drain(5)

    def propel(self, distance:float, depth:float):
        super().move(distance)
        self.change_depth(depth)
        self._sensor.reading = f"{self._depth}m below sea level"


class FlyingRobot(RobotBase):
    """A Flying Robot"""

    def __init__(self, name: str, battery: Battery, motor: Motor, sensor: Sensor, altitude: float):
        """Initialise Flying Robot"""
        super().__init__(name, battery, motor, sensor)
        self._altitude = altitude
        self._sensor.reading = f"{altitude}m high"

    def change_altitude(self, altitude: float):
        if self._altitude == None:
            self._altitude = altitude
        elif(self._altitude + altitude > 0):
            self._altitude += altitude
        else:
            self._altitude = 0
        self._sensor.reading = f"{altitude}m high"
        self._battery.drain(5)

    def propel(self, distance, altitude):
        super().move(distance)
        self.change_altitude(altitude)

# Tests RobotInheritance if is main file   
if __name__ == "__main__":
    Steve = LineFollower("Steve", Battery(75, 75), Motor(0, False), Sensor("Colour Sensor"))
    print(Steve)

    Steve._sensor.reading = "black_line"
    Steve.move(5)
    print(Steve)

    Steve._sensor.reading = "white_line"
    Steve.move(8)
    print(Steve)

    Yellow = SubRobot("Yellow", Battery(100, 100), Motor(0, False), Sensor("Depth Sensor"), 5)
    print(Yellow)

    Yellow.propel(5, 9)
    print(Yellow)

    Clark = FlyingRobot("Clark", Battery(100, 100), Motor(0, False), Sensor("Altitude Sensor"), 0)
    print(Clark)

    Clark.propel(20, 53)
    print(Clark)