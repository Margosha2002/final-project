# final-project

## To run the cli interface run next commands

```
pip3 install -r requirements.txt
python3 scripts/cli.py
```

## Bot commands manual

```
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
```

### Important! After each command the bot will ask you some necessary data to process the command

## To run the api interface with fastAPI graphic interface run next commands

```
pip3 install -r requirements.txt
python3 scripts/api.py
```

Now your graphic interface is running on `http://localhost:3030/docs`
