#!/usr/bin/env python3
'''
Print out a buffet and change it
'''

buffet_foods = ('corn', 'mashed potatoes', 'salsburry steak', 'peas', 'mac and cheese')

for food in buffet_foods:
    print(food)

# buffet_foods[0] = 'broccli' <- this generates and error because tuples are immutable

buffet_foods = ('corn', 'mashed potatoes', 'chicken legs', 'peas', 'rolls')


print("\nThere have been some changes to our menu.\n")
for food in buffet_foods:
    print(food)
