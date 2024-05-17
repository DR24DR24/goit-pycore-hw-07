
import addressbookclasses

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and data please."
        except KeyError:
            return("user is present already")

    return inner

def parse_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("cann't parse")
            return "",""

    return inner

def change_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "user absent"
            #return "no such user"
        except ValueError:
            return "please input <change user_name>"    
    return inner

def phone_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "no such user"
        except IndexError:
            return "please input phone + user name"

    return inner

@input_error
def add_birthday(args, book):
    pass # реалізація

@input_error
def show_birthday(args, book):
    pass # реалізація

@input_error
def birthdays(args, book):
    l=book.get_upcoming_birthdays() # реалізація
    print(l)

@input_error
def add_contact(args, book: addressbookclasses.AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = addressbookclasses.Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@parse_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    book = addressbookclasses.AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(add_contact(args, book))

        elif command == "phone":
            pass# реалізація

        elif command == "all":
            pass# реалізація

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))# реалізація

        elif command == "birthdays":
            print(birthdays(args, book))# реалізація

        else:
            print("Invalid command.")


if __name__=="__main__":
    main()

    

