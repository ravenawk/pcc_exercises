#!/usr/bin/env python3
"""
Defining and using a user class
"""

class User:
    """Class to define a user account"""

    def __init__(self, first, last):
        """Initialize the user"""
        self.first_name = first
        self.last_name = last
        self.full_name = first + " " + last
        self.login_attempts = 0

    def greet_user(self):
        """Greet user"""
        print(f"Hello {self.full_name}!")

    def increment_login_attempts(self):
        """Increase login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0"""
        self.login_attempts = 0

pmartin = User('Pat', 'Martin')
pmartin.greet_user()
print(pmartin.login_attempts)
pmartin.increment_login_attempts()
print(pmartin.login_attempts)
pmartin.increment_login_attempts()
print(pmartin.login_attempts)
pmartin.reset_login_attempts()
print(pmartin.login_attempts)
