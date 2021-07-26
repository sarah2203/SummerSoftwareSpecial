"""
LCHS Python Walkthrough Aug 2021
"""

from person import Person


class Forest:
    """
    A class for exploring the forest
    """

    def __init__(self, player: Person):
        """
        Construct the forest details
        :param player: The Person object for the current player
        """
        self.player = player

    def start(self):
        """
        Start exploring the forest!
        """
        print("Oh no! The forest is scary! Let's go back!! ")
