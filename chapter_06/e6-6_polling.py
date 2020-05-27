
def main():
    favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

    people = ['jen', 'edward', 'phil', 'isabel', 'oscar', 'hector']

    for name in people:
        if name in favorite_languages.keys():
            print(f"Thank you {name} for answering the poll!")
        else:
            print(f"{name}, please feel free to answer the poll :)")

if __name__ == "__main__":
    main()