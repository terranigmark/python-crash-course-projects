from random import choice

class Winner:

    def __init__(self, my_ticket):
        self.options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'E', 'I', 'O', 'U']
        self.my_ticket = my_ticket

    def pick_winner(self):
        winning_ticket = ''
        for option in range(4):
            winning_ticket += str(choice(self.options))

        print(f"The winning ticket is... {winning_ticket}")
        return winning_ticket

    def winner_analysis(self):
        tries = 1
        self.pick_winner()

        while self.my_ticket != self.pick_winner():
            self.pick_winner()
            tries += 1

        print(f"It took {tries} tickets to win!")


first_winner = Winner('1111')
first_winner.pick_winner()
first_winner.winner_analysis()