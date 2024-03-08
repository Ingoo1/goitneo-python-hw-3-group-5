from .input_error import input_error
from .AddressBook import Record


@input_error
def add_contact(args, book):
    if len(args) != 2:
        return "Invalid number of arguments. Usage: add [name] [phone]"

    name, phone = args
    try:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return f"Contact added: {name}"
    except ValueError as e:
        return str(e)
