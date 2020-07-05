#!/usr/bin/env python3

glossary_terms = {
        'elif': 'Another option for a conditional after an if',
        'for': 'Loop over items in a form of count.',
        'if': 'Conditional for make decisions.',
        'print': 'Display something on the screen.',
        'then': 'Option for conditional if "if" is false.'
        }

for key, value in glossary_terms.items():
    print(f"{key}:")
    print(f"  {value}\n")
