#!/usr/bin/env python3
'''
Getting movie tickets a different way
'''

AGE = input("How old are you? (Type 'quit' to quit)")

while AGE != 'quit':
    AGE = int(AGE)
    if AGE < 3:
        print("Your ticket is free!")
    elif AGE < 12:
        print("Your ticket is 10 dollars.")
    else:
        print("Your ticket is 15 dollars.")

    AGE = input("How old are you? (Type 'quit' to quit)")
