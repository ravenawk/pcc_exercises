#!/usr/bin/env python3
"""
Defining and using a user class
"""

class User:
    def __init__(self, first, last, age, sex):
        """Initialize the user"""
       self.first_name = first
       self.last_name = last
       self.age = age
       self.sex = sex

    def describe_user(self):
        """ Describe user """
        print(f"{self.first_name} {self.last_name} is {self.age} years old and
            is a {self.sex}")

    def greet_user(self):
        """Greet user"""
        print(f"Hello {self.first_name}!")


pparker = User('Peter', 
