
def main():
    prompt = "\nWelcome to PyCinemas!"
    print(prompt)

    while True:
        age = int(input("\nWhat's your age?: "))

        if age < 0:
            print("Hmmm... there must be a mistake")
        elif age >= 0 and age < 3:
            print("The ticket is free of charge :)")
        elif age > 2 and age <= 12:
            print("The ticket has a cost of $10")
        elif age > 12:
            print("The ticket has a cost of $15")
        else:
            print("Thanks for your visit")
            break

if __name__ == "__main__":
    main()