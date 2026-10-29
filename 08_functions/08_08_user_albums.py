'''
Haydn Moyer
user albums

'''

def make_album(artist, tracks=None):
    album = {'artist': artist}
    if tracks:
        album['tracks'] = tracks
    return album