#!/usr/bin/env python3
'''
Polling for a dream vacation
'''

places_to_visit = []
poll = input("Where would you like to visit some day? ")

while poll != 'quit':
    places_to_visit.append(poll)
    poll = input("Where would you like to visit one day? (Enter quit to end) ")

for place in places_to_visit:
    print(f"{place.title()} is one of the places people wanted to visit.")
