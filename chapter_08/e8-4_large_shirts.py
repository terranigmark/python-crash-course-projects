
def main():

    def make_shirt(size='large', message='I love Python'):
        print(f"The size of this shirt is {size} and says: {message}")

    def make_medium_shirt(size='medium', message='I love Python'):
        print(f"The size of this shirt is {size} and says: {message}")

    def make_small_shirt(size='small', message='I love Java... j/k'):
        print(f"The size of this shirt is {size} and says: {message}")

    make_shirt()
    make_medium_shirt()
    make_small_shirt()

if __name__ == "__main__":
    main()