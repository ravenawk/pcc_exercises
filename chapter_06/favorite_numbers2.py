#!/usr/bin/env python3
'''
Print out people and their favorite numbers
'''

people_fav_numbers = {
        'john': [2, 222, 22],
        'jessica': [45, 42, 43],
        'jim': [41, 68, 51],
        'junior': [74, 74, 76],
        'jackson': [42, 52, 54]
        }

for name, numbers in people_fav_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are :")
    for number in numbers:
        print(number)
