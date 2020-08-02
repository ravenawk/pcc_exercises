#!/usr/bin/env python3
"""
Showing importing from standard library
"""
from random import randint

class Die():
    """ Roll a die based off of how many sides are passed. 6 is default) """

    def __init__(self, sides=6):
        """Initialize the sides """
        self.sides = sides

    def roll_die(self):
        """ Roll the specific type of die"""
        print(randint(1, self.sides))

six_sided_die = Die()
print("\nSix-sided die")
for i in range(10):
    six_sided_die.roll_die()

ten_sided_die = Die(10)
print("\nTen-sided die")
for i in range(10):
    ten_sided_die.roll_die()

twenty_sided_die = Die(20)
print("\nTwenty-sided die")
for i in range(10):
    twenty_sided_die.roll_die()
