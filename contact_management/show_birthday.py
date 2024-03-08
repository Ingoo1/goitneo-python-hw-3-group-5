from .input_error import input_error


@input_error
def show_birthday(args, book):
    if len(args) != 1:
        return "Invalid number of arguments. Usage: show-birthday [name]"

    name = args[0]
    contact = book.find(name)
    if contact:
        if contact:
            return f"{name}'s birthday is {contact.birthday}."
        else:
            return f"{name} doesn't have a birthday set."
    else:
        return f"Contact {name} not found."
