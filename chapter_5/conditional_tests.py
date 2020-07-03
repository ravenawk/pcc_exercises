#!/usr/bin/env python3
'''
Testing the if statement
'''

CAR = 'subaru'
SOMENO = 42
DESERT = 'cake'
PERSON = 'Peter Parker'
COLOR = 'red'

print("Is the car a subaru? I predict True!")
if CAR == 'subaru':
    print("car == 'subaru'")
print("Is the car a honda? I predict False!")
if CAR != 'honda':
    print("car != 'honda'")

if SOMENO == 42:
    print("It's the correct number")

if SOMENO != 12:
    print("It's not the correct number")

if DESERT == 'cake':
    print("The cake is a lie")

if DESERT != 'pie':
    print("The cake isn't here")

if PERSON.lower() == 'peter parker':
    print("This guy is sticky.")

if PERSON.lower() != 'steve rogers':
    print("This guy isn't the Cap'n.")

if COLOR == 'red':
    print("This color is hot hot hot.")

if COLOR != 'red':
    print("This color is not so hot.")
