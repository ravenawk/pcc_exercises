#!/usr/bin/env python3
import json

fav_number = input("What is your favorite number? ")

with open('fav_number', 'w') as f:
    json.dump(fav_number, f)
    print("Favorite number saved!")
