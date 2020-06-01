
def main():

    def make_sandwich(*ingredients):
        print("Your sandwich will have the following ingredients:")
        for ingredient in ingredients:
            print(f"- {ingredient.title()}")

    make_sandwich('ham', 'cheese')
    make_sandwich('hame', 'cheese', 'mustard', 'bacon', 'avocado')
    make_sandwich('lettuce', 'tomato', 'avocado', 'onion')

if __name__ == "__main__":
    main()