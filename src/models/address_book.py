from .record import Record
from helpers.check_is_match import check_is_match
import json
import os


class ContactNotFoundError(Exception):
    pass


class AddressBook:
    data: list[Record] = []

    filename = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "contacts.json")
    )

    def __init__(self) -> None:
        self.__read()

    def __to_json(self):
        data = []
        for record in self.data:
            data.append(
                {
                    "name": record.name.value,
                    "phone": record.phone.value,
                    "email": record.email.value if record.email else None,
                    "birthday": str(record.birthday) if record.birthday else None,
                    "address": {
                        "country": record.address.country if record.address else None,
                        "city": record.address.city if record.address else None,
                        "street": record.address.street if record.address else None,
                        "house": record.address.house if record.address else None,
                    },
                }
            )
        return json.dumps(data)

    def __from_json(self, dump):
        self.data = [Record(**record) for record in json.loads(dump)]

    def __read(self):
        try:
            with open(self.filename, "r") as file:
                self.__from_json(file.read())
        except:
            pass

    def save(self):
        with open(self.filename, "w+") as file:
            file.write(self.__to_json())

    def add_contact(self, name, address, phone, birthday, email):
        record = Record(name, address, phone, birthday, email)
        self.data.append(record)
        return str(record)

    def change_contact(self, name, field, value):
        record: Record = self.__get_contact(name)

        if field == "address":
            record.add_address(
                value.get("country"),
                value.get("city"),
                value.get("street"),
                value.get("house"),
            )
        elif field == "name":
            record.name = value
        elif field == "phone":
            record.phone = value
        elif field == "email":
            record.email = value
        elif field == "birthday":
            record.birthday = value

        return str(record)

    def show_all(self):
        res = []

        for item in self.data:
            print(str(item))
            res.append(str(item))

        return res

    def find_contacts(self, search):
        res = []

        for record in self.data:
            if (
                check_is_match(record.name.value, search)
                or check_is_match(record.email.value, search)
                or check_is_match(record.phone.value, search)
            ):
                print(str(record))
                res.append(str(record))

        return res

    def __get_contact(self, name):
        for item in self.data:
            if item.name.value == name:
                return item

        raise ContactNotFoundError()

    def get_contact(self, name):
        res = str(self.__get_contact(name))
        print(res)
        return res

    def delete_contact(self, name):
        self.data = list(filter(lambda item: item.name != name, self.data))

    def show_birthdays(self, days):
        res = []

        for item in self.data:
            if item.check_birthday(days):
                print(str(item))
                res.append(str(item))

        return res
