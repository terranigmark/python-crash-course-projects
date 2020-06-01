
def main():

    def make_album(artist_name, album_title, tracks=None):
        return {'artist': artist_name.title(), 'title': album_title.title(), 'tracks': tracks}

    print("Let's create a list of music albums!")

    while True:
        artist_name = input("What's the artist name?: ")
        if artist_name == 'quit':
            break
        album_title = input("What's the album title?: ")
        if album_title == 'quit':
            break
        tracks = int(input("How many tracks does it has?: "))

        print(make_album(artist_name, album_title, tracks))

if __name__ == "__main__":
    main()