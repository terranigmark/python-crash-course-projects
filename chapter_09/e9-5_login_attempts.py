
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


isabel = User('isabel', 'ruiz', 'iris9112', 'isaruiz@email.com', 'colombia')

for i in range(3):
    isabel.increment_login_attempts()

print(isabel.login_attempts)

isabel.reset_login_attempts()
print(isabel.login_attempts)
