
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} hsa about {num_words} words.")

filenames = ['a_tale_of_two_cities.txt', 'little_women.txt', 'plague_of_pythons.txt', 'sharp_eyes.txt', 'alice.txt']

for filename in filenames:
    count_words(filename)