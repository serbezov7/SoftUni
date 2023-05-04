from math import ceil


class PhotoAlbum:
    PHOTOS_ON_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / cls.PHOTOS_ON_PAGE))

    def add_photo(self, label):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < self.PHOTOS_ON_PAGE:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1}" \
                       f" slot {len(self.photos[page])}"
        return "No more free slots"

    def display(self):
        result = ""
        result += "-" * 11 + "\n"
        for page in self.photos:
            result += (len(page) * "[] ").rstrip() + "\n"
            result += "-" * 11 + "\n"
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())