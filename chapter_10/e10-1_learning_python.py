filename = 'python_can_do.txt'

# reading the whole file
with open(filename) as file_object:
    contents = file_object.read()

print(contents)

# reading line by line
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

# reading as a list
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())