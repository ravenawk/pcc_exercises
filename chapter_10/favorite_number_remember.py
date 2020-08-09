#!/usr/bin/env python3
import json

try:
    with open('fav_number.json', 'r') as f:
        fav_number = json.load(f)
        print(fav_number)

except FileNotFoundError:
    print("You haven't given your favorite number yet.")
    fav_number = input("What is your favorite number? ")

    with open('fav_number.json', 'w') as f:
        json.dump(fav_number, f)
        print("Favorite number saved!")


