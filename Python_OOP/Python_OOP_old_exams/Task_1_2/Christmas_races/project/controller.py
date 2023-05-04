from project.Core.create_car import AddCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []  # Car objects
        self.drivers = []  # Driver objects
        self.races = []  # Race objects

        self.add_car = AddCar()

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if any(c.model == model for c in self.cars):
            raise Exception(f"Car {model} is already created!")

        car = self.add_car.adding_new_car(car_type, model, speed_limit)
        if car:
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if any(d.name == driver_name for d in self.drivers):
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if any(r.name == race_name for r in self.races):
            raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver_by_name(driver_name)
        car = self.__find_last_car_by_type(car_type)

        if driver.car is not None:
            old_car = driver.car
            driver.car = car
            car.is_taken = True
            old_car.is_taken = False
            return f"Driver {driver.name} changed his car from {old_car.model} to {car.model}."

        driver.car = car
        car.is_taken = True
        return f"Driver {driver.name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race_by_name(race_name)
        driver = self.__find_driver_by_name(driver_name)

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver.name} is already added in {race.name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_race_by_name(race_name)
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners = sorted(race.drivers, key=lambda driver: -driver.car.speed_limit)
        result = []
        for winner in winners[:3]:
            winner.number_of_wins += 1
            result.append(f"Driver {winner.name} wins the {race.name} race with a speed of {winner.car.speed_limit}.")

        return "\n".join(result)

    def __find_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        raise Exception(f"Driver {driver_name} could not be found!")

    def __find_last_car_by_type(self, car_type):
        for car in self.cars[::-1]:
            if car.__class__.__name__ == car_type:
                if not car.is_taken:
                    return car
        raise Exception(f"Car {car_type} could not be found!")

    def __find_race_by_name(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
        raise Exception(f"Race {race_name} could not be found!")

