#!/usr/bin/env python3

def count_words(filename, word_to_count):
    number_of_word = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        number_of_word += (line.strip().count(word_to_count))

    return number_of_word

list_of_books = ['the_count_of_monte_cristo.txt', 'the_three_musketeers.txt', 'the_time_machine.txt']
for book in list_of_books:
    print(count_words(book,'the '))
