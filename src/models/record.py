from base_classes import Name, Phone, Birthday, Email


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.__birthday = None
        self.__email = None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join([p.value for p in self.phones])}"

    def add_phone(self, phone):
        phone_number = Phone(phone)
        if phone_number.value:
            self.phones.append(phone_number)

    def find_phone(self, phone_number):
        for phone in self.phones:
            if str(phone) == phone_number:
                return phone
        print(
            f"There is no phone number {phone_number} in the {self.name}'s phone list"
        )
        return None

    def edit_phone(self, phone_to_change, new_phone):
        new_phone_number = Phone(new_phone)
        phone = self.find_phone(phone_to_change)
        if phone and new_phone_number.value:
            self.phones = [
                number
                for number in map(
                    lambda i: new_phone_number if str(i) == phone_to_change else i,
                    self.phones,
                )
            ]

    def remove_phone(self, phone_number):
        phone = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)

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
        print("value", value)
        email_value = Email(value)
        if email_value.value:
            self.__email = email_value
