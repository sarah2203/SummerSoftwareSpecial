"""
LCHS Python Walkthrough Aug 2021
"""


class Person:
    """
    A class to represent a person
    """

    def __init__(self, name: str = "", fav_animal: str = ""):
        """
        Construct the person
        :param name: The person's name
        :param fav_animal: The person's favourite animal
        """
        self.name = name
        self.fav_animal = fav_animal
