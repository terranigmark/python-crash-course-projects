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