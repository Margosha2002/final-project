from models.note import Note
from .exceptions import NoteNotFoundError
import json
import os


class NotesBook:
    notes: list[Note] = []

    filename = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "notes.json")
    )

    def __init__(self) -> None:
        self.__read()

    def __to_json(self):
        data = []
        for item in self.notes:
            data.append(
                {
                    "name": item.name,
                    "body": item.body,
                    "tags": item.tags,
                }
            )
        return json.dumps(data)

    def __from_json(self, dump):
        self.notes = [Note(**item) for item in json.loads(dump)]

    def __read(self):
        try:
            with open(self.filename, "r") as file:
                self.__from_json(file.read())
        except:
            pass

    def save(self):
        with open(self.filename, "w+") as file:
            file.write(self.__to_json())

    def add_note(self, name: str, body: str | None, tags: list[str]):
        self.notes.append(Note(name, body, tags))

    def change_note(self, name: str, field: str, value: str | list[str]):
        note = self.__get_note(name)

        if field == "name":
            note.name = value
        elif field == "body":
            note.body = value
        elif field == "tags":
            note.tags = value

    def delete_note(self, name):
        self.notes = list(filter(lambda item: item.name != name, self.notes))

    def show_notes(self):
        for item in self.notes:
            print(str(item))

    def find_notes(self, key):
        for item in self.notes:
            if item.check_key(key):
                print(str(item))

    def get_note(self, name):
        print(str(self.__get_note(name)))

    def __get_note(self, name: str) -> Note:
        for item in self.notes:
            if item.name == name:
                return item

        raise NoteNotFoundError()
