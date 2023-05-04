from project.core.adding_horse import AddHorse
from project.horse_race import HorseRace
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []  # Horse objects
        self.jockeys = []  # Jockeys object
        self.horse_races = []  # HorseRaces objects

        self.add_horse_by_type = AddHorse()

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if any(h.name == horse_name for h in self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")

        horse = self.add_horse_by_type.adding_horse(horse_type, horse_name, horse_speed)
        if horse:
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if any(j.name == jockey_name for j in self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if any(race.race_type == race_type for race in self.horse_races):
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__find_jockey_by_name(jockey_name)
        horse = self.__find_last_horse_by_type(horse_type)

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey.name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.__find_race_by_type(race_type)
        jockey = self.__find_jockey_by_name(jockey_name)
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__find_race_by_type(race_type)
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        best_jockey = sorted(race.jockeys, key=lambda jockey: -jockey.horse.speed)[0]
        return f"The winner of the {race_type} race, with a speed of {best_jockey.horse.speed}km/h is" \
               f" {best_jockey.name}! Winner's horse: {best_jockey.horse.name}."

    def __find_jockey_by_name(self, name):
        for jockey in self.jockeys:
            if jockey.name == name:
                return jockey
        raise Exception(f"Jockey {name} could not be found!")

    def __find_horse_by_type(self, type):
        for horse in self.horses:
            if horse.__class__.__name__ == type:
                return horse
        raise Exception(f"Horse breed {type} could not be found!")

    def __find_last_horse_by_type(self, type):
        for horse in self.horses[::-1]:
            if horse.__class__.__name__ == type:
                if not horse.is_taken:
                    return horse
        raise Exception(f"Horse breed {type} could not be found!")

    def __find_race_by_type(self, type):
        for race in self.horse_races:
            if race.race_type == type:
                return race
        raise Exception(f"Race {type} could not be found!")
































