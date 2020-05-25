
def main():
    current_users = ['iris9112', 'erranigma', 'gndx', 'leonidasesteban', 'hidekoji', 'admin']
    current_users_lowercase = []
    new_users = ['mr_gameover', 'terranigma', 'migueltorresio', 'chinafinanciera', 'Iris9112']

    if new_users == []:
        print('We need to find some users!')

    for user in current_users:
        current_users_lowercase.append(user.lower())

    for user in new_users:
        if user.lower() in current_users_lowercase:
            print(f"The username {user} is already in use, please enter a different one")
        else:
            print(f"The username {user} is available!")

if __name__ == "__main__":
    main()