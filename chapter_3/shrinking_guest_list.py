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

print(f"I am sorry the bigger dinner table won't be delivered in time, and now I only have enough room for two guests.")

print(f"{list_of_guests.pop()} sorry I don't have room.")
print(f"{list_of_guests.pop()} sorry I don't have room.")
print(f"{list_of_guests.pop()} sorry I don't have room.")
print(f"{list_of_guests.pop()} sorry I don't have room.")

print(f"{list_of_guests[0]} you are still invited to dinner.")
print(f"{list_of_guests[1]} you are still invited to dinner.")

del(list_of_guests[0])
del(list_of_guests[0])

print(list_of_guests)
