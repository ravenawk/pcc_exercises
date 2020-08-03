#!/usr/bin/env python3
"""Accept user input and write to a file"""

name = input('Hello, what is your name? ')

with open('guest.txt', 'w') as fileobject:
    fileobject.writelines(name)
