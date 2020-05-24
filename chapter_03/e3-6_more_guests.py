
def main():
    guest_list = ['Era', 'Percy', 'Tomas', 'Tata']

    for guest in range(len(guest_list)):
        print(f'Dear {guest_list[guest]}, you\'re invited to my special dinner so please come!')

    print(f'\nOh, noes!... It seems that {guest_list[-1]} isn\'t coming')

    guest_list[-1] = 'Mirri'

    for guest in range(len(guest_list)):
        print(f'Dear {guest_list[guest]}, you\'re invited to my special dinner so please come!')

    print('Hey, we found a bigger table!')

    guest_list.insert(0, 'Dessa')
    guest_list.insert(2, 'Ric')
    guest_list.append('Subaru')

    for guest in range(len(guest_list)):
        print(f'Dear {guest_list[guest]}, you\'re invited to my special dinner so please come!')

    print('Oh, snap!... We can only have 2 guests :(')

    for guest in range(len(guest_list) - 2):
        print(f'Sorry {guest_list.pop()}, I can not invite you today :(')

    for guest in range(len(guest_list)):
        print(f'Hey {guest_list[guest]}, you are still invited :)')

    for guest in range(len(guest_list)):
        del guest_list[0]

    print(guest_list)

if __name__ == "__main__":
    main()