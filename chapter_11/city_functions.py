#!/usr/bin/env python3

def city_country(city_name, country_name):
    return(f"{city_name.title()}, {country_name.title()}")

if __name__ == '__main__':
    print(city_country('Santiago', 'Chile'))
