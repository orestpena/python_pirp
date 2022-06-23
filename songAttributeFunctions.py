"""

Filename: songAttributeFunctions.py
Title: My favorite song, creating attribute functions.
The 3 attributes are Genre, Artist, and Year.
When the functions are called, it returns the variable
information of my favorite song.
Also for extta credit a boolean function was made that 
returns the opposite boolean of the parameter used.

"""

#My favorite song
song = "If I ever feel better"

#The name of the band
def artist():
    artist_var = "Phoenix"
    return artist_var

#The song's genre
def genre():
    genre_var = "Indie Pop"
    return genre_var

#The name of the album song was released on, date of release, track number on album
def year():
    releaseAlbumDate = "12 June 2000"
    return releaseAlbumDate

#A boolean that returns the opposite boolean value of what the variable is set to.
def trueFalse(variable):
    if variable:
        return False
    return True

print(artist())
print(genre())
print(year())
print(trueFalse(True))
print(trueFalse(False))
