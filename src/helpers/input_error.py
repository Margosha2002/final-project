from models.exceptions import (
    InvalidChangeField,
    InvalidDaysCount,
    NameIsRequiredException,
    PhoneIsRequiredException,
    ContactNotFoundError,
    PhoneValidationError,
    BirthdayValidationError,
    BodyValidationError,
    EmailValidationError,
    NoteNotFoundError,
    TagValidationError,
)
from colorama import Fore


def input_error(func):
    def inner(*args, **kwargs):
        try:
            data = func(*args, **kwargs)
            if data:
                print(data)
        except InvalidDaysCount:
            print(Fore.LIGHTRED_EX + "Invalid days count")
        except NameIsRequiredException:
            print(Fore.LIGHTRED_EX + "Name is required")
        except PhoneIsRequiredException:
            print(Fore.LIGHTRED_EX + "Phone is required")
        except InvalidChangeField:
            print(Fore.LIGHTRED_EX + "Field name is invalid")
        except ContactNotFoundError:
            print(Fore.LIGHTRED_EX + "Contact was not found")
        except PhoneValidationError:
            print(
                Fore.LIGHTRED_EX
                + "Phone number should consists of 10 digits in an international format"
            )
        except BirthdayValidationError:
            print(Fore.LIGHTRED_EX + "Birthday should be in DD.MM.YYYY format")
        except EmailValidationError:
            print(Fore.LIGHTRED_EX + "Please provide valid email address")
        except NoteNotFoundError:
            print(Fore.LIGHTRED_EX + "Note was not found")
        except BodyValidationError:
            print(Fore.LIGHTRED_EX + "Body is invalid")
        except TagValidationError:
            print(Fore.LIGHTRED_EX + "Tag is invalid")
        except Exception:
            print(Fore.LIGHTRED_EX + "Unknown error occurred")

    return inner
