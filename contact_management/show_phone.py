from .input_error import input_error


@input_error
def show_phone(args, book):
    if len(args) != 1:
        return "Invalid number of arguments. Usage: phone [name]"

    name = args[0]
    record = book.find(name)
    if record:
        return record.phones[0].value
    else:
        return f"Contact '{name}' not found."
