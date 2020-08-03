#!/usr/bin/env python3

list_of_guests = ['Arthur Martin Sr.', 'Janet Huertas', 'Grandma Martin']
cant_make_it = list_of_guests.pop()

print(f"{cant_make_it}, can't join us for dinner tonight.\n")

list_of_guests.append('Grandpa Martin')

print(f"{list_of_guests[0]}, please join us for dinner tonight.") 
print(f"{list_of_guests[1]}, please join us for dinner tonight.") 
print(f"{list_of_guests[2]}, please join us for dinner tonight.") 
