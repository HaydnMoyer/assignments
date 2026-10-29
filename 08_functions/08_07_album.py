'''
Haydn Moyer
album

'''

def make_album(artist, tracks=None):
    album = {'artist': artist}
    if tracks:
        album['tracks'] = tracks
    return album

# Example usage:
print(make_album("The Beatles", 17))
print(make_album("Pink Floyd", 10))