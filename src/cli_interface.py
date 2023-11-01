class NameIsRequiredException(Exception):
    pass


class PhoneIsRequiredException(Exception):
    pass


class InvalidDaysCount(Exception):
    pass


class InvalidChangeField(Exception):
    pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            data = func(*args, **kwargs)
            if data:
                print(data)
        except InvalidDaysCount:
            print("Invalid days count")
        except NameIsRequiredException:
            print("Name is required")
        except PhoneIsRequiredException:
            print("Phone is required")
        except InvalidChangeField:
            print("Field name is invalid")
        except Exception:
            print("Unknown error occurred")

    return inner


def on_exit():
    # save to json logic
    print("Good bye!")


def on_greetings():
    print("How can I help you?")


@input_error
def on_add_contact():
    print("Fill all contact info, if you want to leave it blank, just press enter")
    name = input("Enter contact name (required): ")
    if not name:
        raise NameIsRequiredException
    phone = input("Enter phone (required): ")
    if not phone:
        raise PhoneIsRequiredException
    email = input("Enter email: ")
    birthday = input("Enter birthday in DD.MM.YYYY format: ")
    need_fill_address = (
        input("Do you want to fill address details? (Y/N): ").lower() == "y"
    )

    address_details = {"country": "", "city": "", "street": "", "house": ""}

    if need_fill_address:
        address_details["country"] = input("Enter country: ")
        address_details["city"] = input("Enter city: ")
        address_details["street"] = input("Enter street: ")
        address_details["house"] = input("Enter house: ")

    # save into address book logic


@input_error
def on_change_contact():
    contact_name = input("Enter a name of the contact, you need to change: ")

    # find and show contact logic

    field = input(
        "Enter a field, that you need to change (name, phone, email, birthday, address): "
    ).lower()

    if not field in ["name", "phone", "email", "birthday", "address"]:
        raise InvalidChangeField

    if field == "address":
        address_details = {"country": "", "city": "", "street": "", "house": ""}
        address_details["country"] = input("Enter country: ")
        address_details["city"] = input("Enter city: ")
        address_details["street"] = input("Enter street: ")
        address_details["house"] = input("Enter house: ")

        # save into address book logic
    else:
        value = input("Enter field value: ")
        # save into address book logic


def on_show_all_contacts():
    # show contacts logic
    pass


def check_is_match(value, search_pattern):
    string_lower = str(value).lower()
    return string_lower.find(search_pattern.lower()) != -1


# TODO delete (just example of structure)
book = [
    {
        "name": "Anton",
        "email": "agdhdj@djj.com",
        "phone": "8364527842",
    },
    {
        "name": "Alex",
        "email": "alex234@djj.com",
        "phone": "6329013456",
    },
]


# TODO pass an instance of AddressBook class to the function instead of mock
def on_find_contacts():
    search_pattern = input("Enter search pattern: ")
    if search_pattern.strip():
        matches = []
        for record in book:
            if (
                check_is_match(record.name, search_pattern)
                or check_is_match(record.email, search_pattern)
                or check_is_match(record.phone, search_pattern)
            ):
                matches.append(str(record))

        if len(matches):
            matches_string = "\n".join(matches)
            print(f"{'*'*15}\n{matches_string}\n{'*'*15}")
        else:
            print("No matches found")


def on_get_contact():
    name = input("Enter a contact name: ")
    # find and show contact logic


def on_delete_contact():
    name = input("Enter a name of the contact you want to delete: ")
    # find and show contact logic
    is_sure = (
        input(f'Are you sure to delete the contact "{name}"? (Y/N): ').lower() == "y"
    )
    if is_sure:
        # delete contact logic
        pass
    else:
        print("Deletion cancelled!")


@input_error
def on_show_birthdays():
    days = input("Enter days count: ")
    if not days.isdigit():
        raise InvalidDaysCount
    else:
        # show birthdays for next X days
        pass


@input_error
def on_add_note():
    name = input("Enter a name of the note (required): ")
    if not name:
        raise NameIsRequiredException
    body = input("Enter body: ")
    tags = input('Enter tags in "tag1, tag2, tag3" format: ').split(", ")
    # save note logic


@input_error
def on_change_note():
    note_name = input("Enter name of the note you need to change: ")
    # find and show note logic
    field = input("Enter a field, that you need to change (name, body, tags): ").lower()

    if not field in ["name", "body", "tags"]:
        raise InvalidChangeField

    # change note logic


def on_delete_note():
    name = input("Enter a name of the note you want to delete: ")
    # find and show note logic
    is_sure = input(f'Are you sure to delete the note "{name}"? (Y/N): ').lower() == "y"
    if is_sure:
        # delete note logic
        pass
    else:
        print("Deletion cancelled!")


def on_show_notes():
    # show notes logic
    pass


def on_find_notes():
    search_pattern = input("Enter search pattern: ")
    # search note logic


def on_get_note():
    name = input("Enter a note name: ")
    # find and show note logic


def cli_interface():
    # get data from json logic
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").lower()

        if command in ["close", "exit"]:
            on_exit()
            break
        elif command == "hello":
            on_greetings()
        elif command == "add-contact":
            on_add_contact()
        elif command == "change-contact":
            on_change_contact()
        elif command == "show-contacts":
            on_show_all_contacts()
        elif command == "find-contacts":
            on_find_contacts()
        elif command == "get-contact":
            on_get_contact()
        elif command == "delete-contact":
            on_delete_contact()
        elif command == "show-birthdays":
            on_show_birthdays()
        elif command == "add-note":
            on_add_note()
        elif command == "change-note":
            on_change_note()
        elif command == "delete-note":
            on_delete_note()
        elif command == "show-notes":
            on_show_notes()
        elif command == "find-notes":
            on_find_notes()
        elif command == "get-note":
            on_get_note()
        else:
            print("Invalid command.")
