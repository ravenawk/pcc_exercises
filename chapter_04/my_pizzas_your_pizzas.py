#!/usr/bin/env python3

favorite_pizza_types = ['pepperoni', 'mushroom', 'olive']

for pizza in  favorite_pizza_types:
    print(f"I like {pizza} pizza!")

friends_pizza = favorite_pizza_types[:]

favorite_pizza_types.append('green pepper')

friends_pizza.append('sausage')

print(f"Friends list of pizzas is {friends_pizza}.")
print(f"My list of pizzas is {favorite_pizza_types}.")
