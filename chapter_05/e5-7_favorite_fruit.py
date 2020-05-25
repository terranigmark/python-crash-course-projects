
def main():
    favorite_fruits = ['melon', 'watermelon', 'apple', 'pineapple', 'banana', 'cranberry']

    for times in range(5):
        fruit = str(input("Pick a fruit to know if it's on my list: "))

        if fruit in favorite_fruits:
            print(f"You really like {fruit}")

if __name__ == "__main__":
    main()