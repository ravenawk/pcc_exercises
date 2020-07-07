#!/usr/bin/env python3
'''
Get what toppings to put on a pizza.
'''

ADD_TOPPINGS = True

while ADD_TOPPINGS:
    topping = input("What topping would you like on your pizza? (type 'quit' to finsh) ")
    if topping == 'quit':
        print("Here's your pizza.")
        ADD_TOPPINGS = False
    else:
        print(f"Adding {topping} to pizza.")
