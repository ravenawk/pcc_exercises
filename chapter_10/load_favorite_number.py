#!/usr/bin/env python3
import json

try:
    with open('fav_number.json', 'r') as f:
        fav_number = json.load(f)
        print(fav_number)

except FileNotFoundError:
    print("You haven't given your favorite number yet.")

