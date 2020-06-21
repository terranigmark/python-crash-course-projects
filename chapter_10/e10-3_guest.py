
filename = 'guest.txt'

guest_name = input("What's your name?: ")

with open(filename, 'w') as file_object:
    file_object.write(f"{guest_name}")