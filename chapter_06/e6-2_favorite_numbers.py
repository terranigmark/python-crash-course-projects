
def main():
    favorite_numbers = {
        'hector': 8,
        'isabel': 12,
        'oscar': 7,
        'ana': 64,
        'eduardo': 11
    }

    for person in favorite_numbers:
        print(f"{person}'s favorite number is: {favorite_numbers[person]}")

if __name__ == "__main__":
    main()