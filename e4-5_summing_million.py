
def main():
    numbers = [number for number in range(1, 1_000_001)]
    print(min(numbers))
    print(max(numbers))
    print(sum(numbers))

if __name__ == "__main__":
    main()