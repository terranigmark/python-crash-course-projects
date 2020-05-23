# This programs take a number from the user and shows it as it's favorite
def main():
    favorite_number = str(input("What's your favorite number?: "))
    message = f'The number {favorite_number} is awesome!'
    print(message)

if __name__ == "__main__":
    main()