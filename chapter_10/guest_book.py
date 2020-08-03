#!/usr/bin/env python3
"""Accept user input and write to a file"""


with open('guest_book.txt', 'w') as fileobject:
    while True:
        name = input('Hello, what is your name? ')
        if name == 'quit':
            break
        else:
            fileobject.writelines(f"{name}\n")
