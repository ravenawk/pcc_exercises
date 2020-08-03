#!/usr/bin/env python3
'''
Getting movie tickets
'''

GETTING_TICKETS = True

while GETTING_TICKETS:
    age = input("How old are you? (Type 'quit' to quit)")

    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif age < 12:
        print("Your ticket is 10 dollars.")
    else:
        print("Your ticket is 15 dollars.")
