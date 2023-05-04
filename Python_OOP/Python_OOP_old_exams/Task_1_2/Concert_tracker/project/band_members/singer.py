from project.band_members.musician import Musician


class Singer(Musician):
    def __init__(self, name, age):
        super().__init__(name, age)

    @property
    def available_skills(self):
        return ["sing high pitch notes", "sing low pitch notes"]
