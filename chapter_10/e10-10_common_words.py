
def count_word(filename, word):

    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"The file {filename} was not found!")
    else:
        times = contents.lower().count(word)
        print(f"The word {word} appears {times} times in the file {filename}.")

filename = 'a_tale_of_two_cities.txt'
word = input("Enter a word to count how many teams appear in a file: ")

count_word(filename, word)