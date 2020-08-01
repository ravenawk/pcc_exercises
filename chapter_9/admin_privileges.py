#!/usr/bin/env python3
"""
Defining and using a admin subclass with privilege subclass
"""
import create_user

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
