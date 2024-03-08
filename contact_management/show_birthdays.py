def show_birthdays(book):
    birthdays = book.get_birthdays_per_week()
    if birthdays:
        return "\n".join([f"{day}: {', '.join(names)}" for day, names in birthdays.items()])
    else:
        return "No birthdays this week."