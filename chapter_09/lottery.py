#!/usr/bin/env python3
'''
Script to print out random choice of numbers
'''
from random import choice

winning_choice = []
alphanum = ['a', 'b', 'c', 'd', 'e', 1, 3, 4, 5, 6]

for i in range(4):
    single_choice = choice(alphanum)
    alphanum.remove(single_choice)
    winning_choice.append(single_choice)

print(f"The winning numbers are {winning_choice}")
