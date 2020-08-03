#!/usr/bin/env python3
'''
Program for calling and making t-shirts
'''

def make_shirt(size, text):
    '''
    Make the shirt here
    '''
    print(f"One {size} t-shirt with '{text}' printed on the front coming up.")


make_shirt('large', 'Your text here')

make_shirt(size='medium', text='Tux Rocks')
