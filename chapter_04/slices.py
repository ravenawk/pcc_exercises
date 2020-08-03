#!/usr/bin/env python3

list_of_cubes = [ value**3 for value in range(1,11)]

for cube in list_of_cubes:
    print(cube)

print(f"The first 3 items in the list are {list_of_cubes[:3]}.")
print(f"Three items in the middle of the list are {list_of_cubes[3:6]}.")
print(f"The last 3 items in the list are {list_of_cubes[-3:]}.")
