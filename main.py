"""
LCHS Python Walkthrough Aug 2021
"""

from beach import Beach
from forest import Forest
from person import Person


class Game:
    """
    The game!
    """

    def __init__(self):
        """
        Construct the game with default person
        """
        self.player = Person()

    def setup(self):
        """
        Set up the player's details
        """
        username = input("What is your name?")
        fav_animal = input("What's your favourite animal?")
        self.player = Person(username, fav_animal)
        print(f"Hi {self.player.name}! I love {self.player.fav_animal} too! Let's go on an adventure!")

    def start(self):
        """
        Start the game and go to the beach or the forest
        """
        adventure = input("Would you like to go to the beach or the forest?")
        if adventure == "beach":
            Beach(self.player).start()
        elif adventure == "forest":
            Forest(self.player).start()
        else:
            print("Hmmm, I don't know where that is. Let's try again")
            self.start()
        if self.continue_game():
            self.start()

    @staticmethod
    def continue_game() -> bool:
        """
        Ask the user whether they want to keep playing
        :return: True if they want to keep playing
        """
        continue_game = input("Do you want to continue game?")
        if continue_game == "yes":
            return True
        else:
            return False


if __name__ == "__main__":
    game = Game()
    game.setup()
    game.start()
