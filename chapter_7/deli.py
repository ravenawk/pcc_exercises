#!/usr/bin/env python3
'''
Making sandwiches with while loops and for loops
'''

sandwich_orders = ['turkey', 'tuna', 'ham']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich} sandwich.")

for sandwich in finished_sandwiches:
    print(f"A {sandwich} sandwich was made today.")
