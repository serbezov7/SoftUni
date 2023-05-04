from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot


class AddingRobot:
    valid_types = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot,
    }

    def add_new_robot(self, robot_type, name, kind, price):
        if robot_type in self.valid_types:
            return self.valid_types[robot_type](name, kind, price)

        raise Exception("Invalid robot type!")