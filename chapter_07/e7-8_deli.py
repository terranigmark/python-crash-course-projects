
def main():
    sandwiches = ['ham & cheese', 'veggie', 'tuna', 'italian', 'teriyaki chicken']
    finished_sandwiches = []

    while sandwiches:
        made_sandwich = sandwiches.pop()
        finished_sandwiches.append(made_sandwich)
        print(f"I made your {made_sandwich} sandwich")

    print("\nThese sandwiches were made:")
    for sandwich in finished_sandwiches:
        print(sandwich)

if __name__ == "__main__":
    main()