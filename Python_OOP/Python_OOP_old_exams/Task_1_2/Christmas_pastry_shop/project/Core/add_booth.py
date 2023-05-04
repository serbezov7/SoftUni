from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth


class AddBooth:
    booth_types = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth
    }

    def create_booth(self, booth_type, booth_number, capacity):
        if booth_type in self.booth_types.keys():
            return self.booth_types[booth_type](booth_number, capacity)

        raise Exception(f"{booth_type} is not a valid booth!")
