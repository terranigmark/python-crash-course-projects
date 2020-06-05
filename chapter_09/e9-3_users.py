
class User():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

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

isabel = User('Isabel', 'Ruiz', 'iris9112', 'isaruiz@email.com', 'Colombia')

isabel.describe_user()
isabel.greet_user()