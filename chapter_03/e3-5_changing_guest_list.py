
def main():
    guest_list = ['Era', 'Percy', 'Tomas', 'Tata']

    for guest in range(len(guest_list)):
        print(f'Dear {guest_list[guest]}, you\'re invited to my special dinner so please come!')

    print(f'\nOh, noes!... It seems that {guest_list[-1]} isn\'t coming')

    guest_list[-1] = 'Mirri'

    for guest in range(len(guest_list)):
        print(f'Dear {guest_list[guest]}, you\'re invited to my special dinner so please come!')

if __name__ == "__main__":
    main()