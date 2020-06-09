from random import randint

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(f"The {self.sides}-sided die rolled: {randint(1, self.sides)}")

six_sided_die = Die(6)
ten_sided_die = Die(10)
twenty_sided_die = Die(20)

for i in range(10):
    six_sided_die.roll_die()
    ten_sided_die.roll_die()
    twenty_sided_die.roll_die()