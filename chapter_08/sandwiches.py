#!/usr/bin/env python3
'''
Using multiple arguments in a function to build a sandwich
'''

def make_sandwich(*contents):
    ''' Make the sandwich '''
    items = ""
    for item in contents:
        print(f"Adding {item} to your sandwich.")
        if items:
            items = items + f", {item}"
        else:
            items = item
    print(f"We made a sandwitch with {items}.\n")

make_sandwich('turkey', 'swiss', 'tomato')
make_sandwich('roast beef', 'cheddar')
make_sandwich('ham', 'lettuce', 'tomato')
