#!/usr/bin/env python3
'''
Prints out pet types and their owners
'''

zig = {
        'animal': 'cat',
        'owner': 'kyle'
        }
china = {
        'animal': 'dog',
        'owner': 'davie'
        }
lionel = {
        'animal': 'iguana',
        'owner': 'reggie'
        }

pets = [zig, china, lionel]

for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['animal']} as a pet.")
