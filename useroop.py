print(
"""
Module 2 Project
Chelsea Brammer
January 24, 2023
Domain: Horses

""")

# first, import helpful modules to make our job easier

import datetime
import math
import random
from enum import Enum


class Horse_Colors(Enum):
    BAY = 1
    BUCKSKIN = 2
    GRULLA = 3
    PALOMINO = 4


class PyBuddy:
    """ PyBuddy class for creating a study buddy."""

    def __init__(self, name, horse_colors, face_markings, weight_kgs, is_available, skill_list, 
    top_event_scores, num_socks):
        """ Built-in method to create a new instance."""
        self.name = name
        self.horse_colors = horse_colors
        self.face_markings = face_markings
        self.weight_kgs = weight_kgs
        self.is_available = is_available
        self.skill_list = skill_list
        self.create_date = datetime.datetime.now()
        self.top_event_scores = top_event_scores
        self.num_socks = num_socks
      


    def __str__(self):
        """Built-in method to return a string describing this instance"""
        s0 = f"I'm {self.name}.\n"
        s1 = f"I'm a {self.horse_colors} with a {self.face_markings} facial marking.\n"
        s2 = f"I weigh {self.weight_kgs:.2f} kgs.\n"
        s3 = f"I've been alive for {self.get_age_string()}.\n"

        if self.is_available:
            s4 = "I'm available for sale.\n"
        else:
            s4 = "I'm not available for sale.\n"

        s5 = "I know:\n"

        s6 = ""
        for skill in self.skill_list:
            s6 = s6 + f"  - {skill}\n"

        s = s0 + s1 + s2 + s3 + s4 + s5 + s6
        return s

    def get_age_string(self):
        """Return the age as a string."""
        start = self.create_date
        end = datetime.datetime.now()
        duration = end - start
        ageString = str(duration)
        return ageString

    def display_welcome(self):
        print()
        print("Welcome, I'm a new PyBuddy.\n")
        # print using our built-in to string method
        print(self.__str__())
    
    def top_score(self):
        """Return the highest score from top event scores"""
        return max(self.top_event_scores)
    
    def my_socks(self):
        """Return number of leg markings the Horse has"""
        return random.choice(self.num_socks)
        
        final_message = """

        You'll need curiousity, the ability to search the web,
        and the tenacity and resourcefulness
        to solve all kinds of challenges.

        Let's get started!

        """
        print(final_message)


# -------------------------------------------------------------
# Call some functions and execute code!

# if this is the main file being run

if __name__ == "__main__":
    # Create an instance of a PyBuddy
    benny = PyBuddy(
        "Benny",
        Horse_Colors.BUCKSKIN,
        "Stripe",
        456.82356,
        True,
        ["Barrel Pattern", "Team Roping", "Poles", "Calf Roping", "Sorting"],
        ["14.26", "10.4", "11.32", "8.17", "45.32"],
        ["0", "1", "2", "3", "4"]
    )

    # Call the buddy's welcome() method
    benny.display_welcome()

    print()
    print(f"My top score in timed events is {benny.top_score()}")
    print()
    print(f"I have {benny.my_socks()} leg markings")
    print()
 

    # Create another instance of a PyBuddy
    # using named arguments so it's clear what we're doing
    Mouse = PyBuddy(
        name="Mouse", 
        horse_colors= Horse_Colors.GRULLA,
        face_markings= "Star",
        weight_kgs=520.1364,
        is_available=False,
        skill_list=["Barrel Pattern", "Team Roping", "Poles", "Calf Roping", "Penning"],
        top_event_scores=["13.76", "10.6", "12.11", "7.97", "56.19"],
        num_socks= ["0", "1", "2", "3", "4"]
    )

    Mouse.display_welcome()

    print()
    print(f"My highest score from timed events is {Mouse.top_score()}")
    print()
    print(f"I have {Mouse.my_socks()} leg markings")
    print()