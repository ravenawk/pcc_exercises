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

    def describe_restaurant(self):
        """Describe retaurant"""
        print(f"{self.name} is a {self.cuisine} restaurant.")

    def open_restaurant(self):
        """Open retaurant"""
        print(f"{self.name} is open.")


my_restaurant = Restaurant("Miguel's", "Mexican")

print(my_restaurant.name)
print(my_restaurant.cuisine)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

