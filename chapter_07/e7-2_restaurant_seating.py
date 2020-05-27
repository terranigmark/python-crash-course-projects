
def main():
    guests = int(input("For how many people do you want a table?: "))

    if guests < 9:
        print('Your table is ready!')
    else:
        print(f"A table for {guests} people will have to wait...")

if __name__ == "__main__":
    main()