
def main():

    albums = {}

    def make_album(artist_name, album_title, tracks=None):
        return {'artist': artist_name, 'title': album_title, 'tracks': tracks}

    print(make_album('Sylvania', 'Recuerdos del Manniana'))
    print(make_album('Sober', 'Paradysso', 12))
    print(make_album('Saratoga', 'VII', 7))

if __name__ == "__main__":
    main()