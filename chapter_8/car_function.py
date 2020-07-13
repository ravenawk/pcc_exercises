#!/usr/bin/env python3
"""
Module that prints out some cars
"""


def car_info(car_make, car_model, **other_info):
    """ Put together a dictionary for car info"""
    other_info["make"] = car_make
    other_info["model"] = car_model
    return other_info
