
def main():
    person_0 = {
        'first_name': 'Isabel',
        'last_name': 'Ruiz',
        'age': 28,
        'city': 'Bogota'
    }

    person_1 = {
        'first_name': 'Hector',
        'last_name': 'Daniel',
        'age': 30,
        'city': 'La Paz'
    }

    person_2 = {
        'first_name': 'Andres',
        'last_name': 'Ruiz',
        'age': 24,
        'city': 'Tulua'
    }

    people = [person_0, person_1, person_2]

    for person in people:
        for value in person.values():
            print(value)

if __name__ == "__main__":
    main()