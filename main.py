from contact_management.parse_input import parse_input
from contact_management.add_contact import add_contact
from contact_management.change_contact import change_contact
from contact_management.show_phone import show_phone
from contact_management.show_all import show_all
from contact_management.add_birthday import add_birthday
from contact_management.show_birthday import show_birthday
from contact_management.show_birthdays import show_birthdays
from contact_management.AddressBook import AddressBook, Record


def main():

    # Для тесту
    book = AddressBook()
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_birthday('11.03.1988')

    # Додавання запису John до адресної книги
    book.add_record(john_record)
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "bye", "bb"]:
            print("Good bye!")
            break
        elif command in ["hello", "hi", "yo"]:
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(show_birthdays(book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

