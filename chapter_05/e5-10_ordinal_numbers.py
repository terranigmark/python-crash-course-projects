
def main():
    numbers = [number for number in range(1, 10)]
    print(numbers)

    for number in numbers:
        if number == 1:
            print(f"{number}st")
        elif number == 2:
            print(f"{number}nd")
        elif number == 3:
            print(f"{number}rd")
        else:
            print(f"{number}th")

if __name__ == "__main__":
    main()