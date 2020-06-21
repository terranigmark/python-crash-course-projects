import json



def get_stored_favorite_number():
    """Get user's favorite number stored"""

    filename = 'favorite_number.json'

    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        None
    else:
        return favorite_number

def get_new_favorite_number():
    """Get user's favorite number"""

    filename = 'favorite_number.json'

    try:
        favorite_number = int(input("What's your favorite number?: "))
    except ValueError:
        print("Your input wasn't a number!")
    else:
        with open(filename, 'w') as f:
            json.dump(favorite_number, f)

        return favorite_number

def show_favorite_number():
    """prints user's favorite number"""

    favorite_number = get_new_favorite_number()

    if favorite_number:
        print(f"Your favorite number is {favorite_number}")
    else:
        favorite_number = get_new_favorite_number()
        print(f"Your favorite number was stored as {favorite_number}")

show_favorite_number()