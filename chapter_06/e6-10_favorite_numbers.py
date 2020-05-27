
def main():
    favorite_numbers = {
        'hector': [8, 64, 42, 4],
        'isabel': [12, 5, 20],
        'oscar': [7, 33, 19],
        'ana': [4, 76, 100],
        'eduardo': [120, 68, 47]
    }

    for person in favorite_numbers.keys():
        print(f"{person}'s favorite numbers are:")
        for number in favorite_numbers[person]:
            print(f"\t{number}")

if __name__ == "__main__":
    main()