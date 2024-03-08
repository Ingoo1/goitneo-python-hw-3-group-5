from .input_error import input_error


def change_contact(args, book):
    if len(args) != 2:
        return "Invalid number of arguments. Usage: change [name] [new_phone]"

    name, new_phone = args
    record = book.find(name)
    if record:
        try:
            record.edit_phone(record.phones[0].value, new_phone)
            return f"Phone number updated for {name}."
        except ValueError as e:
            return str(e)
    else:
        return f"Contact '{name}' not found."
