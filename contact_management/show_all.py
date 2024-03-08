from .input_error import input_error


@input_error
def show_all(book):
    if len(book) == 0:
        return "Address book is empty."

    result = ""
    for record in book.values():
        result += str(record) + "\n"
    return result.strip()

