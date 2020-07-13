#!/usr/bin/env python3
"""
Function that prints out some cars
"""
import cars as ci

my_car = ci.car_info("Ford", "Mustang", color="blue", interior="cloth")

for key, value in my_car.items():
    print(f"{key} : {value}")
