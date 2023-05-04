from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)

    def drive(self, kilometers):
        if kilometers * self.DEFAULT_FUEL_CONSUMPTION <= self.fuel:
            self.fuel -= kilometers * self.DEFAULT_FUEL_CONSUMPTION
