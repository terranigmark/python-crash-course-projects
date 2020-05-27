
def main():
    number = int(input("Give me a number to know if it's multiple of ten: "))
    module_of_ten = number % 10

    if module_of_ten == 0:
        print(f"The number {number} is a multiple of 10!")
    else:
        print(f"The number {number} is NOT a multiple of 10!")

if __name__ == "__main__":
    main()