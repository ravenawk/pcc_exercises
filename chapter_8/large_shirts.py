#!/usr/bin/env python3
'''
Program for calling and making t-shirts
'''

def make_shirt(size='large', text='I love Python'):
    '''
    Make the shirts
    '''
    print(f"One {size} t-shirt with '{text}' printed on the front coming up.")


make_shirt()
make_shirt('medium')
make_shirt(size='small', text='Tux Rocks')
