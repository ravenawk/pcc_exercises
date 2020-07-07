#!/usr/bin/env python3
'''
Print out some peoples favorite places
'''

fav_places = {
        'charlie': ['mammoth', 'phoenix', 'glendora park'],
        'yvonne': ['rock creek lake', 'la jolla', 'oray'],
        'pat': ['denver', 'mammoth', 'renton']
        }
for person, places in fav_places.items():
    print(f"\n{person.title()}'s favorite places are: ")
    for place in places:
        print(f"{place.title()}")
