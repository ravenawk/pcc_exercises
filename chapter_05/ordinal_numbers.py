#!/usr/bin/env python3
'''
Print out ordinal numbers
'''

ordinal_list = list(range(1, 10))

for number in ordinal_list:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
