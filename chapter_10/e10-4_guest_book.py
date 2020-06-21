
keep_adding = True
filename = 'guest.txt'

while keep_adding:
    guest_name = input("What's your name?: ")
    print(f"{guest_name}, thanks for your visit!")

    with open(filename, 'a') as file_object:
        file_object.write(f"{guest_name}\n")

    another_guest = input("Do you with to add another record? (y/n): ")

    if another_guest.lower() == 'n':
        keep_adding = False