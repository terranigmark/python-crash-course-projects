
def main():
    pet_0 = {
        'name': 'percy',
        'owner': 'isabel'
    }

    pet_1 = {
        'name': 'tomas',
        'owner': 'reynaldo'
    }

    pet_2 = {
        'name': 'elmo',
        'owner': 'oscar'
    }

    pet_3 = {
        'name': 'pepito',
        'owner': 'luisa'
    }

    pets = [pet_0, pet_1, pet_2, pet_3]

    for pet in pets:
        for key, value in pet.items():
            print(key, value)

if __name__ == "__main__":
    main()