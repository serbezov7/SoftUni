import random


class Game:
    def __init__(self, max_attempts=3):
        self.max_attempts = max_attempts
        self.number = random.randint(1, 10)
        self.won = False
        self.attempts = 0

    def guess(self, number):
        self.attempts += 1
        if self.number == number:
            self.won = True
            print("Congratulations You Won!")
        if self.attempts < 3:
            if self.number > number:
                print("Sorry, You have to try again with bigger number")
            elif self.number < number:
                print("Sorry, You have to try again with lower number")
        elif not self.won:
            print(f"Sorry Yoy have lost. The number was {self.number}.")


game = Game()
while game.attempts != 3 and not game.won:
    number = int(input("Please choose a number: "))
    game.guess(number)

