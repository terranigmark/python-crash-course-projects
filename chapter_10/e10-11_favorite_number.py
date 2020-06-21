import json

filename = 'favorite_number.json'

try:
    favorite_number = int(input("What's your favorite number?: "))
except ValueError:
    print("Your input wasn't a number!")
else:
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)

    print(f"Favorite number stored in {filename} as {favorite_number}")