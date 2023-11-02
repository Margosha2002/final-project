class NameIsRequiredException(Exception):
    pass


class PhoneIsRequiredException(Exception):
    pass


class InvalidDaysCount(Exception):
    pass


class InvalidChangeField(Exception):
    pass


class PhoneValidationError(Exception):
    pass


class BirthdayValidationError(Exception):
    pass


class EmailValidationError(Exception):
    pass


class BodyValidationError(Exception):
    pass


class TagValidationError(Exception):
    pass


class NoteNotFoundError(Exception):
    pass


class ContactNotFoundError(Exception):
    pass