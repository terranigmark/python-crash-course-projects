
def adding_continously(number):

    result = 0

    while True:
        try:
            number = int(input("Enter a number to add: "))
        except ValueError:
            print(f'''
                Verify that your input is a number
            ''')
        else:
            result += number
            print(f"You've added so far: {result}")

number = 0

adding_continously(number)