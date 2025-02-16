def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Invalid command format."
    return inner

contacts = {}

@input_error
def add_contact(args):
    if len(args) < 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args):
    if len(args) < 1:
        raise IndexError
    name = args[0]
    return contacts[name]

@input_error
def show_all(args):
    if not contacts:
        return "No contacts saved."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    while True:
        command = input("Enter a command: ").strip().lower()
        
        if command == "exit":
            print("Goodbye!")
            break
        elif command.startswith("add"):
            args = command.split()[1:]
            print(add_contact(args))
        elif command.startswith("phone"):
            args = command.split()[1:]
            print(get_phone(args))
        elif command == "all":
            print(show_all([]))
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
