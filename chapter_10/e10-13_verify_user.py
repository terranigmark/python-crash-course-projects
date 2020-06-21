import json

# load the username, if it has been stored previously.
# otherwise, prompt for the username and store it

def get_stored_username():
    """Get stored username if available"""

    filename = 'username.json'

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username"""

    username = input("What is your name?: ")
    filename = 'username.json'

    with open(filename, 'w') as f:
        json.dump(username, f)

    return username

def greet_user():
    """Greet user by name"""

    while True:
        username = get_stored_username()
        validate_user = input(f"Are you {username}? (y/n): ")

        if validate_user.lower() == 'n':
            get_new_username()
            continue
        else:
            break

    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()