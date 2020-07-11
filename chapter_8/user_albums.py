#!/usr/bin/env python3
'''
Function example of record album
'''

def make_album(artist_name, album_title, song_count=None):
    ''' Create album information '''
    album = {'artist': artist_name, 'album name': album_title,}
    if song_count:
        album['number of songs'] = song_count
    return album

while True:
    ARTIST = input("What is the artis's name? (enter quit to exit) ")
    if ARTIST == 'quit':
        break
    ALBUM = input("What is the album's name? ")
    print(make_album(ARTIST, ALBUM))
