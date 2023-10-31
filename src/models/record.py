from base_classes import Name, Phone, Birthday, Email, Address


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.address = None
        self.__phone = None
        self.__birthday = None
        self.__email = None

    def __str__(self):
        email_str = str(self.__email) if self.__email else "---"
        phone_str = str(self.__phone) if self.__phone else "---"
        return f"Name: {self.name.value:<12}, phone: {phone_str:<12}, email: {email_str:<12}".format()

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        phone_value = Phone(value)
        if phone_value.value:
            self.__phone = phone_value

    def remove_phone(self):
        self.__phone = None

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        birthday_value = Birthday(value)
        if birthday_value.value:
            self.__birthday = birthday_value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        email_value = Email(value)
        if email_value.value:
            self.__email = email_value

    def add_address(self, city, street, house, flat=None):
        address = Address(city, street, house, flat)
        self.address = address
