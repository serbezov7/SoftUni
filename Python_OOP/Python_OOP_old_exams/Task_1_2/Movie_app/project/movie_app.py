from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []  # Movies objects
        self.users_collection = []  # Users objects

    def register_user(self, username: str, age: int):
        if any(u.username == username for u in self.users_collection):
            raise Exception("User already exists!")

        user = User(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_name(username)
        if not user:
            raise Exception("This user does not exist!")

        self.__check_is_owner(username, movie)

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        self.__check_is_owner(username, movie)

        for attribute, value in kwargs.items():
            if attribute == "title":
                movie.title = value
            elif attribute == "year":
                movie.year = value
            elif attribute == "age_restriction":
                movie.age_restriction = value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        self.__check_is_owner(username, movie)

        user = self.__find_user_by_name(username)
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        self.__check_is_same_owner(username, movie)

        user = self.__find_user_by_name(username)
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        user.movies_liked.append(movie)
        movie.likes += 1
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_name(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        sorted_movies = sorted(self.movies_collection, key=lambda movie: (-movie.year, movie.title))
        if not sorted_movies:
            return "No movies found."
        return "\n".join(movie.details() for movie in sorted_movies)

    def __str__(self):
        result = ""
        if not self.users_collection:
            result += "All users: No users.\n"
        else:
            users = ", ".join(user.username for user in self.users_collection)
            result += "All users: " + users + "\n"

        if not self.movies_collection:
            result += "All movies: No movies."
        else:
            movies = ", ".join(movie.title for movie in self.movies_collection)
            result += "All movies: " + movies

        return result

    def __find_user_by_name(self, name):
        for user in self.users_collection:
            if user.username == name:
                return user

    @staticmethod
    def __check_is_owner(username, movie):
        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

    @staticmethod
    def __check_is_same_owner(username, movie):
        if username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")


