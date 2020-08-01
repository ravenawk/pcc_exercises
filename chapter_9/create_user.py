#!/usr/bin/env python3
"""
Defining and using a user class with admin subclass
"""


class User:
    """Class to define a user account"""

    def __init__(self, first, last):
        """Initialize the user"""
        self.first_name = first
        self.last_name = last
        self.full_name = first + " " + last

    def describe_user(self):
        """ Describe user """
        print(f"{self.first_name} {self.last_name} is a user on the system.")

    def greet_user(self):
        """Greet user"""
        print(f"Hello {self.full_name}!")
