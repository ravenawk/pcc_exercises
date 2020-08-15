#!/usr/bin/env python3

def city_country_population(city_name, country_name, population=None):
    if population:
        return(f"{city_name.title()}, {country_name.title()} - {population}")
    else:
        return(f"{city_name.title()}, {country_name.title()}")


if __name__ == '__main__':
    print(city_country_population('Santiago', 'Chile', 5000000))
