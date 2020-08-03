#!/usr/bin/env python3

my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]

for food in my_foods:
    print(f"My favorite foods are {food}")

print("\n")

for food in friend_foods:
    print(f"My friends favorite foods are {food}")
