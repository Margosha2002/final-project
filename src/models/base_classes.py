import re
from datetime import datetime


class PhoneValidationError(Exception):
    pass


class BirthdayValidationError(Exception):
    pass


class EmailValidationError(Exception):
    pass


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        # acceptable formats 1111111111, (111)111-1-111, 111-111-11-11, (111)111-11-11
        valid_phone_number = re.match(
            r"(^[(]?[\d]{3}[)\-]?[\d]{3}[-]?[\d]{2}[-]?[\d]{2}$)|(^[(]?[\d]{3}[)\-]?[\d]{3}[-]?[\d]{1}[-]?[\d]{3}$)",
            phone,
        )

        if not valid_phone_number:
            raise PhoneValidationError(
                "Phone number should consists of 10 digits in international format"
            )

        super().__init__(phone)


class Birthday(Field):
    def __init__(self, birthday):
        # acceptable format "DD.MM.YYYY"
        valid_format = re.match(
            r"^(0[1-9]|1\d|2\d|3[01])\.(0[1-9]|1[0-2])\.(19|20)\d{2}$", birthday
        )

        if not valid_format:
            raise BirthdayValidationError("Birthday should be in DD.MM.YYYY format")

        birthday_date = datetime.strptime(birthday, "%d.%m.%Y").date()
        super().__init__(birthday_date)


class Email(Field):
    def __init__(self, email):
        valid_email = re.match(r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$", email)

        if not valid_email:
            raise EmailValidationError("Please provide valid email address")

        super().__init__(email)
