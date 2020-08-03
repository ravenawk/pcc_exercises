#!/usr/bin/env python3
'''
Display points for two different colors
'''

ALIEN_COLOR = 'green'

if ALIEN_COLOR == 'green':
    print(f"You hit a {ALIEN_COLOR} and got 5 points!")
else:
    print(f"You hit a {ALIEN_COLOR} and got 10 points!")

ALIEN_COLOR = 'red'

if ALIEN_COLOR == 'green':
    print(f"You hit a {ALIEN_COLOR} and got 5 points!")
else:
    print(f"You hit a {ALIEN_COLOR} and got 10 points!")
