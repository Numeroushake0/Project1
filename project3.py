def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args


@input_error
def add_contact(args, contacts):
    name, phone = args  
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone  
    return "Number updated."


@input_error
def show_phone(args, contacts):
    name = args[0]  
    return contacts[name]  


@input_error
def show_all(contacts):
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items()) or "The contact list is empty."


def main():
    contacts = {}
    print("How can I help you?")
    while True:
        user_input = input("Enter your command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Thank you for using the bot! Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Unknown command. Use one of the following commands: add, change, phone, all, close, exit.")


if __name__ == "__main__":
    main()