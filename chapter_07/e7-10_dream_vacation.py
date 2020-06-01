
def main():
    destinations = {}
    active = True

    while active:
        name = input("What's your name?: ")
        destination = input("Where would be your dream vacation?: ")

        destinations[name] = destination

        repeat = input("Would you like to let another person answer? (yes/no): ")

        if repeat == 'no':
            active = False

    print("\n--- Poll Results ---")

    for name, destination in destinations.items():
        print(f"{name.title()}'s dream vacation is in {destination.title()}")

if __name__ == "__main__":
    main()