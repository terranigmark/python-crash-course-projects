
def read_pet_names():

    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"The file {filename} was not found")
    else:
        print(f"\nHere are the contents of the file {filename}:\n{contents}")

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    read_pet_names()