"""
LCHS Python Walkthrough Aug 2021
"""

from random import randrange
from typing import List


class Beach:
    """
    A class for having fun at the beach
    """

    def __init__(self, player):
        """
        Construct the information about the beach
        :param player: The Person object for the current player
        """
        self.player = player

        self.sun_shining = True
        self.tide_out = True

        self.sunset = randrange(start=4, stop=10)
        self.tide = randrange(start=4, stop=10)

        self.time = 0

    def start(self):
        """
        Start investigating the beach
        """
        print("Welcome to the beach!")

        print("The sun is shining and the tide is out!")
        print("However, if this changes it'll be time to leave the beach.")

        while self.sun_shining and self.tide_out:
            self.play()
            self.increment_time()

        if not self.sun_shining:
            print("The sun's gone in. Let's go home.")
            return
        if not self.tide_out:
            print("The tide came in. We have to leave the beach.")

    def play(self):
        """
        Go play on the beach
        """
        print("What would you like to do?")

        # This is a dictionary used to select an activity
        activities = {"a": "build sandcastles", "b": "swim", "c": "sunbathe"}
        for activity_key in activities.keys():
            print(activity_key + ": " + activities[activity_key])

        chosen_activity_key = input()
        if chosen_activity_key not in activities.keys():
            print("Hmmm, I don't recognise that option...")
            self.play()
        chosen_activity = activities[chosen_activity_key]
        print(f"Great!! Let's {chosen_activity}")

        if chosen_activity == "build sandcastles":
            self.build_sandcastles()
        elif chosen_activity == "swim":
            self.swim()
        elif chosen_activity == "sunbathe":
            self.sunbathe()

        self.increment_time()

    def build_sandcastles(self):
        """
        Build a sandcastles
        """
        print(f"I see your favourite animal is a {self.player.fav_animal}.")
        fav_animal_sandcastle = input(f"Shall we build a {self.player.fav_animal} sandcastle?")
        if fav_animal_sandcastle == "yes" or fav_animal_sandcastle == "Yes":
            print(f"Built {self.player.fav_animal} sandcastle")
        else:
            sandcastle = input("Ok, what shall we build a sandcastle of?")
            print(f"Built {sandcastle} sandcastle")

    def swim(self):
        """
        Go for a swim
        """
        print("Get in the sea!")
        stroke = input("What stroke shall we swim?")
        if stroke == "butterfly":
            print("SHAAARRRRKKKKKKKK!!!")
            print("Quick get out the water!")
            return
        print("What a lovely day!")
        print("Let's do something else!")

    def sunbathe(self):
        """
        Sunbathe - Make sure to apply suncream
        """
        bag_contents = ["keys", "suncream", "wallet"]
        self.apply_suncream(bag_contents)

    def apply_suncream(self, bag_items: List[str]):
        """
        Apply suncream
        :param bag_items: The items in your bag
        :return: When you've applied your suncream
        """
        print("Let's have a look in your bag and see what we'll need to sunbathe.")
        print(bag_items)
        item = input("What do we need?")
        if item == "suncream":
            print("Always good to be protected from the sun!")
            return
        elif item not in bag_items:
            print("Weird. I can't see that in your bag. Have another look.")
        else:
            print("That's not very useful right now!")
            bag_items.remove(item)
        self.apply_suncream(bag_items)

    def increment_time(self):
        """
        Tick tock...
        """
        self.time += 1
        if self.time > self.sunset:
            self.sun_shining = False
        if self.time > self.tide:
            self.tide_out = False
