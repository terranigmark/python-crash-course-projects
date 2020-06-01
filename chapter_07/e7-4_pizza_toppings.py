
def main():
    pizza_toppings = []

    prompt = 'Welcome to our pizza restaurant!'
    prompt += '\nEnter "quit" when you don\'t want more toppings'
    print(prompt)

    while True:
        new_topping = input("\nPlease input a topping for your pizza: ").lower()

        if new_topping == 'quit':
            break
        else:
            print(f'\n {new_topping} is a great choice!')
            pizza_toppings.append(new_topping)
            print("So far your pizza has:")
            for topping in range(len(pizza_toppings)):
                print(pizza_toppings[topping])

if __name__ == "__main__":
    main()