#!/usr/bin/env python3
"""
Function that prints out some cars
"""
import car_function

my_car = car_function.car_info("Ford", "Mustang", color="blue", interior="cloth")

for key, value in my_car.items():
    print(f"{key} : {value}")
