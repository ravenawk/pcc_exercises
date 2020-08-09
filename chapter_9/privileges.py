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


class Privileges:
    """Set privileges for user admin"""

    def __init__(self):
        """initialize privileges"""
        self.abilities = ["can add post", "can delete post", "can ban user"]

    def describe_privileges(self):
        """Describe privileges for user admin"""
        print(f"{ self.full_name } can:")
        for ability in self.abilities:
            print(f"- {ability}")


class Admin(User):
    """Class to define admin subclass"""

    def __init__(self, first, last):
        """Initialize admin"""
        User.__init__(self, first, last)
        super().__init__(first, last)
        self.privileges = Privileges()

the_admin = Admin("Reed", "Richards")

the_admin.describe_user()
the_admin.greet_user()
the_admin.privileges()
