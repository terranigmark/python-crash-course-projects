
def main():
    name = '\tHector\n'
    rstrip_name = name.rstrip()
    lstrip_name = name.lstrip()
    strip_name = name.strip()

    message = f'''
    Your name applying different strip methods are...
    Right strip: {rstrip_name}
    Left strip: {lstrip_name}
    Strip both sides: {strip_name}
    '''

    print(message)


if __name__ == "__main__":
    main()