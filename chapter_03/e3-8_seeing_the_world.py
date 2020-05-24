
def main():
    locations = ['La Paz', 'Tulua', 'Buenos Aires', 'Ireland', 'Tokyo', 'Brussels']
    print(locations)
    print(sorted(locations))
    print(locations)
    print(sorted(locations, reverse=True))
    print(locations)
    locations.reverse()
    print(locations)
    locations.reverse()
    print(locations)
    locations.sort()
    print(locations)
    locations.sort(reverse=True)
    print(locations)

if __name__ == "__main__":
    main()