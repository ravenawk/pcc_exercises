#!/usr/bin/env python3
"""
Defining and using a user class
"""

class User:
    """Class to define a user account"""

    def __init__(self, first, last, age, sex):
        """Initialize the user"""
        self.first_name = first
        self.last_name = last
        self.age = age
        self.sex = sex
        self.full_name = first + " " + last

    def describe_user(self):
        """ Describe user """
        print(f"{self.first_name} {self.last_name} is {self.age} years old and"
            f" is a {self.sex}")

    def greet_user(self):
        """Greet user"""
        print(f"Hello {self.full_name}!")


pparker = User('Peter', 'Parker', 25, 'male')
mjane = User('Mary', 'Jane', 25, 'female')
srogers = User('Steve', 'Rogers', 85, 'male')

pparker.describe_user()
mjane.greet_user()
srogers.describe_user()
