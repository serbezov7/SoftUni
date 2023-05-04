from project.add_musicians import AddMusician
from project.band import Band
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands = []  # Bands objects
        self.musicians = []  # Musicians objects
        self.concerts = []  # Concerts objects

        self.add_musician = AddMusician()

    @staticmethod
    def __find_musicians_who_is_member_of_band(name, band):
        for musician in band.members:
            if musician.name == name:
                return musician
        raise Exception(f"{name} isn't a member of {band.name}!")

    def __find_concert_by_place(self, place):
        for concert in self.concerts:
            if concert.place == place:
                return concert

    def __find_musician_by_name(self, name):
        for musician in self.musicians:
            if musician.name == name:
                return musician
        raise Exception(f"{name} isn't a musician!")

    def __find_band_by_name(self, name):
        for band in self.bands:
            if band.name == name:
                return band
        raise Exception(f"{name} isn't a band!")

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.add_musician.musician_types:
            raise ValueError("Invalid musician type!")
        if any(m.name == name for m in self.musicians):
            raise Exception(f"{name} is already a musician!")
        musician = self.add_musician.add_musician(musician_type, name, age)

        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if any(b.name == name for b in self.bands):
            raise Exception(f"{name} band is already created!")
        band = Band(name)

        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")
        concert = Concert(genre, audience, ticket_price, expenses, place)

        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.__find_musician_by_name(musician_name)
        band = self.__find_band_by_name(band_name)
        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.__find_band_by_name(band_name)
        musician = self.__find_musicians_who_is_member_of_band(musician_name, band)

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self.__find_band_by_name(band_name)
        concert = self.__find_concert_by_place(concert_place)

        for musician_type in ["Drummer", "Singer", "Guitarist"]:
            if not any(filter(lambda x: x.__class__.__name__ == musician_type, band.members)):
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        # drummer = 0
        # singer = 0
        # guitarist = 0
        #
        # for member in band.members:
        #     if member.__class__.__name__ == "Drummer":
        #         drummer += 1
        #     elif member.__class__.__name__ == "Singer":
        #         singer += 1
        #     elif member.__class__.__name__ == "Guitarist":
        #         guitarist += 1
        # if not drummer or not singer or not guitarist:
        #     raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            for member in band.members:
                if member.__class__.__name__ == "Drummer":
                    if "play the drums with drumsticks" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == "Singer":
                    if "sing high pitch notes" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == "Guitarist":
                    if "play rock" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Metal":
            for member in band.members:
                if member.__class__.__name__ == "Drummer":
                    if "play the drums with drumsticks" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == "Singer":
                    if "sing low pitch notes" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == "Guitarist":
                    if "play metal" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Jazz":
            for member in band.members:
                if member.__class__.__name__ == "Drummer":
                    if "play the drums with drum brushes" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == "Singer":
                    if "sing high pitch notes" not in member.skills or \
                            "sing low pitch notes" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == "Guitarist":
                    if "play jazz" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
