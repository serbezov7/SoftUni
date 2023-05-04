from project.Core.adding_robot import AddingRobot
from project.Core.adding_service import AddingService


class RobotsManagingApp:
    def __init__(self):
        self.robots = []  # Robots objects
        self.services = []  # Service objects

        self.add_another_service = AddingService()
        self.add_another_robot = AddingRobot()

    def add_service(self, service_type: str, name: str):
        service = self.add_another_service.add_new_service(service_type, name)

        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        robot = self.add_another_robot.add_new_robot(robot_type, name, kind, price)

        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.__find_robot_by_name(robot_name)
        service = self.__find_service_by_name(service_name)

        validation = self.__check_can_be_added(robot, service)
        if validation:
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.__find_service_by_name(service_name)

        robot = self.__find_robot_by_name_in_service(service, robot_name)

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.__find_service_by_name(service_name)

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.__find_service_by_name(service_name)

        total_price = sum(r.price for r in service.robots)

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []

        for service in self.services:
            result.append(service.details())

        return "\n".join(result)

    def __find_robot_by_name(self, name):
        for robot in self.robots:
            if robot.name == name:
                return robot

    def __find_service_by_name(self, name):
        for service in self.services:
            if service.name == name:
                return service

    @staticmethod
    def __find_robot_by_name_in_service(service, name):
        for robot in service.robots:
            if robot.name == name:
                return robot

        raise Exception("No such robot in this service!")

    @staticmethod
    def __check_can_be_added(robot, service):
        if robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ != "SecondaryService":
            return "Unsuitable service."

        elif robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ != "MainService":
            return "Unsuitable service."



