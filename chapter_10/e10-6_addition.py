
try:
    first_number = int(input("Enter a number: "))
    second_number = int(input("Enter a second number to add: "))
except ValueError:
    print(f'''
        Verify that your inputs are numbers
    ''')
else:
    result = print(f"The result is {first_number + second_number}")