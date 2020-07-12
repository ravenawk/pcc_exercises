#!/usr/bin/env python3
"""
Function that prints out some cars
"""


def car_info(car_make, car_model, **other_info):
    """ Put together a dictionary for car info"""
    other_info["make"] = car_make
    other_info["model"] = car_model
    return other_info


my_car = car_info("Ford", "Mustang", color="blue", interior="cloth")

for key, value in my_car.items():
    print(f"{key} : {value}")
