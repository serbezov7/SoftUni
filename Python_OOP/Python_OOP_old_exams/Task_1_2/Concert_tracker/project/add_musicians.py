from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer


class AddMusician:

    musician_types = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }

    def add_musician(self, musician_type, name, age):
        return self.__class__.musician_types[musician_type](name, age)
