
def main():

    def show_messages(message_list):
        while messages:
            outgoing_message = messages.pop()
            print(f"Sending: {outgoing_message}")
            sent_messages.append(outgoing_message)

            print(f"Pending messages: {messages}")
            print(f"Sent messages: {sent_messages}")

    messages = ['ola ke ase', 'bienvenido al mundo real', 'saldo insuficiente']
    sent_messages = []

    show_messages(messages)

if __name__ == "__main__":
    main()