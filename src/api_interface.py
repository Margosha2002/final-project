from fastapi import FastAPI
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
import uvicorn
from pydantic import BaseModel
from enum import Enum
from models.address_book import AddressBook
from models.notes_book import NotesBook

app = FastAPI()

helloRouter = APIRouter()
contactsRouter = APIRouter()
notesRouter = APIRouter()

contacts = AddressBook()
notes = NotesBook()


class AddressModel(BaseModel):
    country: str | None = None
    city: str | None = None
    street: str | None = None
    house: str | None = None


class PostContactRequest(BaseModel):
    name: str
    address: AddressModel | None = None
    phone: str
    email: str | None = None
    birthday: str | None = None


class PutContactFields(str, Enum):
    name = "name"
    phone = "phone"
    email = "email"
    birthday = "birthday"
    address = "address"


class PutContactRequest(BaseModel):
    field: PutContactFields
    value: str | AddressModel


class PostNoteRequest(BaseModel):
    name: str
    body: str
    tags: list[str]


class PutNoteFields(str, Enum):
    name = "name"
    body = "body"
    tags = "tags"


class PutNoteRequest(BaseModel):
    field: PutNoteFields
    value: str | list[str]


@helloRouter.get("")
async def hello():
    return JSONResponse({"result": "How can I help you?", "success": True})


@contactsRouter.get("")
async def get_contacts():
    return JSONResponse({"result": contacts.show_all(), "success": True})


@contactsRouter.post("")
async def post_contact(body: PostContactRequest):
    return JSONResponse(
        {"result": contacts.add_contact(**body.dict()), "success": True}
    )


@contactsRouter.put("/{name}")
async def put_contact(name: str, body: PutContactRequest):
    return JSONResponse(
        {"result": contacts.change_contact(name, **body.dict()), "success": True}
    )


@contactsRouter.get("/find/{search}")
async def find_contacts(search: str):
    return JSONResponse({"result": contacts.find_contacts(search), "success": True})


@contactsRouter.get("/birthdays")
async def get_birthdays(days: int):
    return JSONResponse({"result": contacts.show_birthdays(days), "success": True})


@contactsRouter.get("/{name}")
async def get_contact(name: str):
    return JSONResponse({"result": contacts.get_contact(name), "success": True})


@contactsRouter.delete("/{name}")
async def delete_contact(name: str):
    contacts.delete_contact(name)
    return JSONResponse({"success": True})


@notesRouter.get("")
async def get_notes():
    return JSONResponse({"result": notes.show_notes(), "success": False})


@notesRouter.post("")
async def add_note(body: PostNoteRequest):
    return JSONResponse({"result": notes.add_note(**body.dict()), "success": True})


@notesRouter.put("/{name}")
async def put_note(name: str, body: PutContactRequest):
    return JSONResponse(
        {"result": notes.change_note(name, **body.dict()), "success": True}
    )


@notesRouter.delete("/{name}")
async def delete_note(name: str):
    notes.delete_note(name)
    return JSONResponse({"success": True})


@notesRouter.get("/find/{search}")
async def find_notes(search: str):
    return JSONResponse({"result": notes.find_notes(search), "success": True})


@notesRouter.get("/{name}")
async def get_note(name: str):
    return JSONResponse({"result": notes.get_note(name), "success": True})


@app.on_event("shutdown")
async def shutdown():
    contacts.save()
    print("Contacts saved")


app.include_router(router=helloRouter, prefix="/hello", tags=["hello"])
app.include_router(router=contactsRouter, prefix="/contacts", tags=["contacts"])
app.include_router(router=notesRouter, prefix="/notes", tags=["notes"])


def main():
    uvicorn.run(app=app, port=3030)


if __name__ == "__main__":
    main()
