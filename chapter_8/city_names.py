#!/usr/bin/env python3
'''
Generate a function for printing a city and its country
'''

def city_country(city_name, country_name):
    '''Print city, country'''
    print(f"{city_name.title()}, {country_name.title()}")

city_country('Mammoth', 'USA')
city_country('Tokyo', 'Japan')
city_country('Dublin', 'Ireland')
