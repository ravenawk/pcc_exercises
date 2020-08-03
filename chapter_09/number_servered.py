#!/usr/bin/env python3
"""
Describe and define a restaurant
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
        print(f"{self.name} is a {self.cuisine} restaurant.")

    def open_restaurant(self):
        """Open retaurant"""
        print(f"{self.name} is open.")

    def set_number_served(self, num_served):
        """Set the number of people served to a specific number"""
        self.number_servered = num_served

    def increment_number_served(self, additional_num_served):
        """Set the number of people served to a specific number"""
        self.number_servered += additional_num_served

my_restaurant = Restaurant("Miguel's", "Mexican")

print(my_restaurant.number_servered)
my_restaurant.number_servered = 9
print(my_restaurant.number_servered)
my_restaurant.set_number_served(10)
print(my_restaurant.number_servered)
my_restaurant.increment_number_served(2)
print(my_restaurant.number_servered)
