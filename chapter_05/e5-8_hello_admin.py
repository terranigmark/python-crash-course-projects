
def main():
    usernames = ['iris9112', 'terranigma', 'gndx', 'leonidasesteban', 'hidekoji', 'admin']

    for user in usernames:
        if user == 'admin':
            print('Hello admin, would you like to see a report?')
        else:
            print(f"Hello {user}, thank you for logging again!")

if __name__ == "__main__":
    main()