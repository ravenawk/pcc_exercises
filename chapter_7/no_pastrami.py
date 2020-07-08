#!/usr/bin/env python3
'''
Making sandwiches with while loops and for loops but out of pastrami
'''

sandwich_orders = ['pastrami', 'turkey', 'pastrami', 'tuna', 'pastrami', 'ham']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich} sandwich.")

for sandwich in finished_sandwiches:
    print(f"A {sandwich} sandwich was made today.")
