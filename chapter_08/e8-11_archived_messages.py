
def main():

    def show_messages(messages):
        print("Showing al messages")
        for message in messages:
            print(message)

    def send_messages(messages, sent_messages):
        print("\nSending al messages")

        while messages:
            outgoing_message = messages.pop()
            print(outgoing_message)
            sent_messages.append(outgoing_message)

    messages = ['ola ke ase', 'bienvenido al mundo real', 'saldo insuficiente']
    show_messages(messages)

    sent_messages = []
    send_messages(messages, sent_messages)

if __name__ == "__main__":
    main()