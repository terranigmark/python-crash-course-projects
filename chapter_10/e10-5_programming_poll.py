
keep_asking = True
filename = 'poll_results.txt'

while keep_asking:
    reason = input("Tell us, why do you love programming?: ")

    with open(filename, 'a') as file_object:
        file_object.write(f"{reason}\n")

    ask_again = input("Do you wish to add another reason? (y/n): ")

    if ask_again.lower() == 'n':
        keep_asking = False