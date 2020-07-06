#!/usr/bin/env python3
'''
Represent people in a dictionary
'''

jan = {
    'first_name': 'Janet',
    'last_name': 'Huertas',
    'city': 'Fontana',
    'age' : 68
    }

david = {
    'first_name': 'David',
    'last_name': 'Martin',
    'city': 'Riverside',
    'age': 61
    }

art = {
    'first_name': 'Arthur',
    'last_name': 'Martin',
    'city': 'Oak Glen',
    'age': 72
    }

people_info = [jan, david, art]

for person in people_info:
    print(person['first_name'])
    print(person['last_name'])
    print(person['city'])
    print(person['age'])
