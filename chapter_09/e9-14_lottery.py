from random import choice

# options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'E', 'I', 'O', 'U']

class Winner:

    def __init__(self):
        self.options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'E', 'I', 'O', 'U']

    def pick_winner(self):
        winning_ticket = ''
        for option in range(4):
            winning_ticket += str(choice(self.options))

        print(f"The winning ticket is... {winning_ticket}")

first_winner = Winner()
first_winner.pick_winner()