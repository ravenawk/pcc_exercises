#!/usr/bin/env python3
'''
Check if there is a wait for restaurant seating
'''

people_amount = int(input("How many people dining tonight? "))

if people_amount <= 8:
    print("Your table is ready.")
else:
    print("There is currently a wait for tables that large.")
