
def main():
    cities = {
        'la paz': {
            'country': 'mexico',
            'population': 224219,
            'fact': 'most popular street food are hot dogs'
        },

        'california': {
            'country': 'united states of america',
            'population': 415800,
            'fact': 'is the largest municipality in valle del cauca'
        },

        'los cabos': {
            'country': 'mexico',
            'population': 238487,
            'fact': 'it has connection with 3 differents seas'
        }
    }

    for city, data in cities.items():
        print(f"Here's some information about {city}")
        for data, information in data.items():
            print(f"{data}: {information}")

if __name__ == "__main__":
    main()