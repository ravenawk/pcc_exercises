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

miguels = Restaurant("Miguel's Jr", "Mexican")
panda = Restaurant("Panda Express", "Chinese")
portillos = Restaurant('Portillos', 'Chicagian')

miguels.describe_restaurant()
panda.describe_restaurant()
portillos.describe_restaurant()
