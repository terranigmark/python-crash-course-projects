
def main():

    def make_car(manufacturer, model, **optionals):
        optionals['manufacturer'] = manufacturer
        optionals['model'] = model
        return optionals

    subaru_outback = make_car(
        'subaru',
        'outback',
        color = 'blue',
        doors = 4
    )

    volskwagen_beetle = make_car(
        'volsk wagen',
        'beetle',
        color = 'black',
        doors = 2
    )

    honda_city = make_car(
        'honda',
        'city',
        color = 'silver',
        doors = 4
    )

    print(subaru_outback)
    print(volskwagen_beetle)
    print(honda_city)

if __name__ == "__main__":
    main()