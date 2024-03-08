def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please. Format: str(name) int(phone)"
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Invalid command format."

    return inner
