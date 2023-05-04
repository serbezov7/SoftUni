class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age
        self.movies_liked = []  # Movies objects
        self.movies_owned = []  # Movies objects

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        result = ""
        result += f"Username: {self.username}, Age: {self.age}\n"

        result += "Liked movies:\n"
        result_liked = '\n'.join(movie.details() for movie in self.movies_liked)
        result += result_liked if result_liked else "No movies liked."
        result += "\n"

        result += "Owned movies:\n"
        result_owned = '\n'.join(movie.details() for movie in self.movies_owned)
        result += result_owned if result_owned else "No movies owned."

        return result
