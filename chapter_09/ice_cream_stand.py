#!/usr/bin/env python3
"""
Describe and define a restaurant and then a child class
"""


class Restaurant:
    """A model of a restaurant"""

    def __init__(self, name, cuisine):
        """Initialize restaurant info"""
        self.name = name
        self.cuisine = cuisine
        self.number_servered = 0

    def describe_restaurant(self):
        """Describe retaurant"""
        print(f"{self.name} serves {self.cuisine} dishes.")

    def open_restaurant(self):
        """Open retaurant"""
        print(f"{self.name} is open.")

    def set_number_served(self, num_served):
        """Set the number of people served to a specific number"""
        self.number_servered = num_served

    def increment_number_served(self, additional_num_served):
        """Set the number of people served to a specific number"""
        self.number_servered += additional_num_served


class IceCreamStand(Restaurant):
    """model of an ice cream stand"""

    def __init__(self, name, cuisine="ice cream"):
        """initialize flavor's available"""
        super().__init__(name, cuisine)
        self.flavors = ["chocolate", "vanilla", "strawberry"]

    def show_flavors(self):
        """Show all the flavors available"""
        print(f"The following flavors are available {self.flavors}")


my_icecream_parlor = IceCreamStand("Handles")
my_icecream_parlor.show_flavors()
my_icecream_parlor.describe_restaurant()
