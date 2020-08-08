#!/usr/bin/env python3
# This is a duplicate because I already wrote what this exercie wanted
"""Add two numbers while checking for valid characters being passed"""

def addition(num1, num2):
    """Add two numbers with exception handling"""
    try:
        return int(num1) + int(num2)
    except ValueError:
        return "Please input numbers only."

while True:
    number1 = input("Input a number to add (q to quit) ")
    if number1 == 'q':
        break
    number2 = input("Input another number to add (q to quit) ")
    if number2 == 'q':
        break
    print(addition(number1, number2))
