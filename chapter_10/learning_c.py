#!/usr/bin/env python3

with open('can_do_in_python.txt') as fileobject:
    lines = fileobject.readlines()

for line in lines:
    print(line.replace('Python','C').strip())

print("")