
def main():

    def favorite_book(book):
        print(f"One of my favorite books is {book.title()}")

    book = input("What's your favorite book?: ")

    favorite_book(book)

if __name__ == "__main__":
    main()