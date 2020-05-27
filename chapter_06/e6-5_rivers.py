
def main():
    rivers = {
        'amazonas': 'brazil',
        'nile': 'egypt',
        'yangtse': 'china',
        'missisipi': 'us'
    }

    for river, country in rivers.items():
        print(f"The {river} river is the longest in {country}.")

    print("The lonngest rivers in the world are:")
    for river in rivers.keys():
        print(river)

    print("The countries with the longest rivers in the world are:")
    for country in rivers.values():
        print(country)

if __name__ == "__main__":
    main()