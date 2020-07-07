#!/usr/bin/env python3
'''
Three cities and some info about them
'''

cities_info = {
        'New York': {
            'state': 'New York',
            'population': 8_300_000,
            'fact': '5 boroughs'
            },
        'Chicago': {
            'state': 'Illinois',
            'population': 2_700_000,
            'fact': 'On lake michigan'
            },
        'Denver': {
            'state': 'Colorado',
            'population': 619_000,
            'fact': 'Mile high city'
            }
        }

for city, info in cities_info.items():
    print(f"The city is {city} and its info is: ")
    for key, item in info.items():
        print(f"\t{key} : {item}")
