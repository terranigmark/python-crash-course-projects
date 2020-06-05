
class User():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f'''
        === Here is the user data ===
        First name: {self.first_name}
        Last name: {self.last_name}
        Username: {self.username}
        Email: {self.email}
        Location: {self.location}
        ''')

    def greet_user(self):
        print(f"Hi {self.first_name}! How are you doing?")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.permissions = Privileges()


class Privileges:

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can edit post']

    def show_privileges(self):
        print("These are the admin privileges:")

        for privilege in self.privileges:
            print(f"\t{privilege}")


#isabel = User('isabel', 'ruiz', 'iris9112', 'isaruiz@email.com', 'colombia')
isabel = Admin('isabel', 'ruiz', 'iris9112', 'isaruiz@email.com', 'colombia')
isabel.permissions.show_privileges()