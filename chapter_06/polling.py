#!/usr/bin/env python3
'''
List people's favorite programming languages
'''

favorite_language = {
        'jen': 'pyhton',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

list_of_people = ['jen', 'scott', 'sarah', 'art', 'edward', 'phil']

for person in list_of_people:
    if person in favorite_language.keys():
        print(f"{person.title()} thank you for taking the poll.")
    else:
        print(f"{person.title()} please take our poll.")
