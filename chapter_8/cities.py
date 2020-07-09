#!/usr/bin/env python3
'''
Description of city
'''

def describe_city(city, country='Ireland'):
    '''
    Display city and country
    '''
    print(f"{city} is in {country}.")

describe_city('Denver', 'United States')
describe_city('Dublin')
describe_city('Paris', 'France')
