
def main():
    name = str(input("What's your name?: "))
    upper_name = name.upper()
    lower_name = name.lower()
    title_name = name.title()

    message = f'''
    Your name in different cases are...
    {upper_name}
    {lower_name}
    {title_name}
    '''

    print(message)

if __name__ == "__main__":
    main()