from abc import ABC, abstractmethod

from project.user import User


class Movie(ABC):
    def __init__(self, title, year, owner: User, age_restriction):
        self.title = title
        self.year = year
        self.owner = owner  # User object
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    @abstractmethod
    def get_genre(self):
        pass

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("The title cannot be empty string!")
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if value.__class__.__name__ != "User":
            raise ValueError("The owner must be an object of type User!")
        self.__owner = value

    def details(self):
        return f"{self.get_genre} - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"
