from base_classes import Name, Phone, Birthday, Email, Address


class Record:
    def __init__(self, name, address, phone, birthday, email):
        self.__name = Name(name)
        if address:
            self.address = Address(
                address.get("country"),
                address.get("city"),
                address.get("street"),
                address.get("house"),
            )
        else:
            self.address = None
        self.__phone = Phone(phone) or None
        self.__birthday = Birthday(birthday) or None
        self.__email = Email(email) or None

    def __str__(self):
        email_str = str(self.__email) if self.__email else "---"
        phone_str = str(self.__phone) if self.__phone else "---"
        birthday_str = str(self.__birthday) if self.__birthday else "---"
        return f"Name: {str(self.__name)<12}, phone: {phone_str:<12}, email: {email_str:<12}, birthday: {birthday_str:<12}".format()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        name_value = Name(value)
        if name_value.value:
            self.__name = name_value

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
