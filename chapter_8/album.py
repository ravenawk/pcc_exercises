#!/usr/bin/env python3
'''
Function example of record album
'''

def make_album(artist_name, album_title, song_count=None):
    ''' Create album information '''
    album = {'artist': artist_name, 'album name': album_title}
    if song_count:
        album['number of songs'] = song_count
    return album

print(make_album('Police', 'Synchronicity', 11))
print(make_album('Beattles', 'A Hard Days Night'))
print(make_album('Led Zeppelin', 'Houses of the Holy'))
