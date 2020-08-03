#!/usr/bin/env python3
"""
Function that prints out some cars
"""
from car_function import car_info

my_car = car_info("Ford", "Mustang", color="blue", interior="cloth")

for key, value in my_car.items():
    print(f"{key} : {value}")
