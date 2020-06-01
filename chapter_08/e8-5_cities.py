
def main():

    def describe_city(city, country='Mexico'):
        print(f"{city} is in {country}")

    describe_city('La Paz')
    describe_city('Guadalajara')
    describe_city('Tulua', 'Colombia')

if __name__ == "__main__":
    main()