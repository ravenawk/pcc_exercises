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


class Admin(User):
    """Class to define admin subclass"""

    def __init__(self, first, last):
        """Initialize admin"""
        User.__init__(self, first, last)
        self.privileges = Privileges()

class Privileges:
    """Class for listing privileges"""

    def __init__(self, privileges=[]):
        """Initialize privileges"""
        self.privileges = privileges

    def set_privileges(self, *list_of_privs):
        """Set privileges"""
        for priv in list_of_privs:
            self.privileges.append(priv)

    def describe_privileges(self):
        """Show privileges for user admin"""
        if self.privileges:
            for priv in self.privileges:
                print(f"- {priv}")
        else:
            print("This user doesn't have any privileges")


if __name__ == '__main__':
    the_admin = Admin("Reed", "Richards")
    the_admin.describe_user()
    the_admin.greet_user()
    the_admin.privileges.describe_privileges()
    the_admin.privileges.set_privileges("can update users name", "can update users profiles", "can change users password")
    the_admin.privileges.describe_privileges()

