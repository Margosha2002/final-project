from models.exceptions import (
    InvalidDaysCount,
    InvalidChangeField,
)
from models.notes_book import NotesBook
from models.address_book import AddressBook
from helpers.input_error import input_error
from helpers.create_prompt import create_prompt
from helpers.required_input import required_input
from colorama import Fore


def on_exit(
    contacts: AddressBook,
    notes: NotesBook,
):
    contacts.save()
    notes.save()
    print("Good bye!")


def on_greetings(*args, **kwargs):
    print("How can I help you?")


@input_error
def on_add_contact(contacts: AddressBook, *args, **kwargs):
    print("Fill all contact info, if you want to leave it blank, just press enter")
    name = required_input("Enter contact name (required): ", "Name is required")
    phone = required_input("Enter phone (required): ", "Phone is required")
    email = input("Enter email: ").strip()
    birthday = input("Enter birthday in DD.MM.YYYY format: ").strip()
    need_fill_address = (
        input("Do you want to fill address details? (y/N): ").strip().lower() == "y"
    )

    address_details = {"country": "", "city": "", "street": "", "house": ""}

    if need_fill_address:
        address_details["country"] = input("Enter country: ").strip()
        address_details["city"] = input("Enter city: ").strip()
        address_details["street"] = input("Enter street: ").strip()
        address_details["house"] = input("Enter house: ").strip()

    contacts.add_contact(name, address_details, phone, birthday, email)
    print("Contact added")


@input_error
def on_change_contact(contacts: AddressBook, *args, **kwargs):
    contacts.show_all()

    contact_name = input("Enter a name of the contact, you need to change: ").strip()

    contacts.get_contact(contact_name)

    field = (
        input(
            "Enter a field, that you need to change (name, phone, email, birthday, address): "
        )
        .strip()
        .lower()
    )

    if not field in ["name", "phone", "email", "birthday", "address"]:
        raise InvalidChangeField()

    if field == "address":
        address_details = {"country": "", "city": "", "street": "", "house": ""}
        address_details["country"] = input("Enter country: ").strip()
        address_details["city"] = input("Enter city: ").strip()
        address_details["street"] = input("Enter street: ").strip()
        address_details["house"] = input("Enter house: ").strip()

        contacts.change_contact(contact_name, field, address_details)
    else:
        value = input("Enter field value: ").strip()
        contacts.change_contact(contact_name, field, value)

    print("Contact changed")


def on_show_all_contacts(contacts: AddressBook, *args, **kwargs):
    contacts.show_all()


def on_find_contacts(contacts: AddressBook, *args, **kwargs):
    search_pattern = input("Enter search pattern: ").strip()
    contacts.find_contacts(search_pattern)


@input_error
def on_get_contact(contacts: AddressBook, *args, **kwargs):
    name = input("Enter a contact name: ").strip()
    contacts.get_contact(name)


@input_error
def on_delete_contact(contacts: AddressBook, *args, **kwargs):
    name = input("Enter a name of the contact you want to delete: ").strip()
    contacts.get_contact(name)
    is_sure = (
        input(f'Are you sure to delete the contact "{name}"? (y/N): ').strip().lower()
        == "y"
    )
    if is_sure:
        contacts.delete_contact(name)
        print("Contact deleted")
    else:
        print("Deletion cancelled!")


@input_error
def on_show_birthdays(contacts: AddressBook, *args, **kwargs):
    days = input("Enter days count: ").strip()
    if not days.isdigit():
        raise InvalidDaysCount()
    else:
        contacts.show_birthdays(int(days))
        pass


@input_error
def on_add_note(notes: NotesBook, *args, **kwargs):
    name = required_input("Enter a name of the note (required): ", "Name is required")
    body = input("Enter body: ").strip()
    tags = input('Enter tags in "tag1, tag2, tag3" format: ').strip().split(", ")
    notes.add_note(name, body, tags)
    print("Note added")


@input_error
def on_change_note(notes: NotesBook, *args, **kwargs):
    notes.show_notes()
    note_name = input("Enter name of the note you need to change: ").strip()
    notes.get_note(note_name)
    field = (
        input("Enter a field, that you need to change (name, body, tags): ")
        .strip()
        .lower()
    )

    if not field in ["name", "body", "tags"]:
        raise InvalidChangeField()

    value = input("Enter field value: ").strip()

    notes.change_note(note_name, field, value if field != "tags" else value.split(", "))
    print("Note changed")


@input_error
def on_delete_note(notes: NotesBook, *args, **kwargs):
    name = input("Enter a name of the note you want to delete: ").strip()
    notes.get_note(name)
    is_sure = (
        input(f'Are you sure to delete the note "{name}"? (y/N): ').strip().lower()
        == "y"
    )
    if is_sure:
        notes.delete_note(name)
        print("Note deleted")
    else:
        print("Deletion cancelled!")


def on_show_notes(notes: NotesBook, *args, **kwargs):
    notes.show_notes()


def on_find_notes(notes: NotesBook, *args, **kwargs):
    search_pattern = input("Enter search pattern: ").strip().lower()
    notes.find_notes(search_pattern)


@input_error
def on_get_note(notes: NotesBook, *args, **kwargs):
    name = input("Enter a note name: ").strip()
    notes.get_note(name)


def show_command_list(*args, **kwargs):
    print(
        """
    *************************************************************************
    hello               -->  to greet an assistant
    help                -->  to get the list of possible commands
    add-contact         -->  to add a contact with further instractions
    change-contact      -->  to change the contact with further instractions
    show-contacts       -->  to display the whole contact list
    find-contacts       -->  to display contacts by provided symbols
    get-contact         -->  to display contact's data
    delete-contact      -->  to delete provided contact
    show-birthdays      -->  to display contacts' bithdays
    add-note            -->  to add a note
    change-note         -->  to change a note
    delete-note         -->  to delete a note
    show-notes          -->  to display notes list
    find-notes          -->  to display notes by provided symbols
    get-note            -->  to display a note
    exit | close        -->  to exit and store contacts
    *************************************************************************
    """
    )


COMMANDS = {
    "close": on_exit,
    "exit": on_exit,
    "hello": on_greetings,
    "help": show_command_list,
    "add-contact": on_add_contact,
    "change-contact": on_change_contact,
    "show-contacts": on_show_all_contacts,
    "find-contacts": on_find_contacts,
    "get-contact": on_get_contact,
    "delete-contact": on_delete_contact,
    "show-birthdays": on_show_birthdays,
    "add-note": on_add_note,
    "change-note": on_change_note,
    "delete-note": on_delete_note,
    "show-notes": on_show_notes,
    "find-notes": on_find_notes,
    "get-note": on_get_note,
}


def cli_interface():
    contacts = AddressBook()
    notes = NotesBook()

    print("Welcome to the assistant bot!")
    show_command_list()

    command_list = COMMANDS.keys()

    while True:
        command = create_prompt(command_list).lower().strip()

        if command in COMMANDS:
            COMMANDS[command](contacts=contacts, notes=notes)

            if command in ["close", "exit"]:
                break
        else:
            print(
                Fore.YELLOW
                + "Invalid command. Type"
                + Fore.LIGHTGREEN_EX
                + ' "help" '
                + Fore.YELLOW
                + "to get the whole command list"
            )


if __name__ == "__main__":
    cli_interface()
