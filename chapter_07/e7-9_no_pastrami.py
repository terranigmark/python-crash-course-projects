
def main():
    sandwiches = ['pastrami', 'ham & cheese', 'veggie', 'pastrami', 'tuna', 'italian', 'teriyaki chicken', 'pastrami']
    finished_sandwiches = []

    while sandwiches:
        if 'pastrami' in sandwiches:
            sandwiches.remove('pastrami')
        else:
            made_sandwich = sandwiches.pop()
            finished_sandwiches.append(made_sandwich)
            print(f"I made your {made_sandwich} sandwich")

    print("\nThese sandwiches were made:")
    for sandwich in finished_sandwiches:
        print(sandwich)

if __name__ == "__main__":
    main()