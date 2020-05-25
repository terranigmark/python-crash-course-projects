
def main():
    odd_numbers = [number for number in range(1, 20, 2)]

    for number in odd_numbers:
        print(number)

    print(f"This list has {len(odd_numbers)}")
    print(f"The first three items in the list are: {odd_numbers[:3]}")
    print(f"The three items from the middle of the list are: {odd_numbers[4:7]}")
    print(f"The last three items in the list are: {odd_numbers[-3:]}")

if __name__ == "__main__":
    main()