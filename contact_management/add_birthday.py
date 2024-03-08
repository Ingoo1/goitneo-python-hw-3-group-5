from .input_error import input_error


@input_error
def add_birthday(args, book):
    if len(args) != 2:
        return "Invalid number of arguments. Usage: add-birthday [name] [birthday]"

    name, birthday = args
    contact = book.find(name)
    if contact:
        contact.add_birthday(birthday)
        return f"Birthday added for {name}."
    else:
        return f"Contact {name} not found."
