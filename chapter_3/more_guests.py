#!/usr/bin/env python3

list_of_guests = ['Arthur Martin Sr.', 'Janet Huertas', 'Grandma Martin']

print(f"I have found a bigger dinner table")

print(f"{list_of_guests[0]}, please join us for dinner tonight.")
print(f"{list_of_guests[1]}, please join us for dinner tonight.") 
print(f"{list_of_guests[2]}, please join us for dinner tonight.")

list_of_guests.insert(0,'Grandpa Martin')
list_of_guests.insert(2,'Aunt Ruth')
list_of_guests.append('Aunt Grace')

print(f"{list_of_guests[0]}, please join us for dinner tonight.")
print(f"{list_of_guests[1]}, please join us for dinner tonight.")
print(f"{list_of_guests[2]}, please join us for dinner tonight.")
print(f"{list_of_guests[3]}, please join us for dinner tonight.")
print(f"{list_of_guests[4]}, please join us for dinner tonight.")
print(f"{list_of_guests[5]}, please join us for dinner tonight.")
