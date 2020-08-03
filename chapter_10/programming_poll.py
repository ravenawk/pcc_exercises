#!/usr/bin/env python3
"""Accept user input and write to a file"""


with open('programming_poll.txt', 'w') as fileobject:
    while True:
        result = input('Hello, why do you like to program? (enter "quit" to end)')
        if result == 'quit':
            break
        else:
            fileobject.writelines(f"{result}\n")
