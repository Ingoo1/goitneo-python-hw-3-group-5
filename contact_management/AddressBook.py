from collections import UserDict
from datetime import datetime, timedelta
from collections import defaultdict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must contain 10 digits.")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Birthday must be in the format DD.MM.YYYY.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phone_numbers = '; '.join(str(p) for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phone_numbers}, birthday: {self.birthday}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_birthdays_per_week(self):
        birthdays_per_week = defaultdict(list)
        today = datetime.today().date()

        for record in self.values():
            if record.birthday:
                birthdate = datetime.strptime(record.birthday.value, '%d.%m.%Y').date()
                birthday_this_year = birthdate.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                delta_days = (birthday_this_year - today).days

                if 0 <= delta_days < 7:
                    birthday_weekday = (today + timedelta(days=delta_days)).strftime("%A")
                    if birthday_weekday in {"Saturday", "Sunday"}:
                        birthday_weekday = "Monday"

                    birthdays_per_week[birthday_weekday].append(record.name.value)

        return birthdays_per_week

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())




# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_birthday('11.03.1988')

# Додавання запису John до адресної книги
book.add_record(john_record)


# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
jane_record.add_birthday('13.03.1988')

book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.items():
    print(record)

print(book.get_birthdays_per_week())

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555


# Видалення запису Jane
book.delete("Jane")