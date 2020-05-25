
def main():
    my_pizzas = ['carnes frias', 'vegetariana', 'pepperoni']
    friend_pizzas = my_pizzas[:]

    my_pizzas.append('chilaquiles')
    friend_pizzas.append('neapolitan')

    print("May favorite pizzas are:")
    for pizza in my_pizzas:
        print(pizza)

    print("My friend's favorite pizzas are:")
    for pizza in friend_pizzas:
        print(pizza)

    print('I REALLY LOVE PIZZA!')

if __name__ == "__main__":
    main()