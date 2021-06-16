from nanohttp import HTTPKnownStatus, settings


class StatusInvalidStringType(HTTPKnownStatus):
    status = '400 Invalid type for username'


class StatusUsernameLengthInvalid(HTTPKnownStatus):
    status = '400 Usernam Lenght Must Be Greater Than 3' \
             'Characters Less than 15 Character'


class StatusUsernameIsRequired(HTTPKnownStatus):
    status = '400 Username is required'


class StatusUsernameIsNull(HTTPKnownStatus):
    status = '400 Username is null'


class StatusFirstnameIsNull(HTTPKnownStatus):
    status = '400 Firstname field is null'


class StatusLastnameIsNull(HTTPKnownStatus):
    status = '400 Lastname field is null'


class StatusRepetitiveUsername(HTTPKnownStatus):
    status = '400 Username is already exist'

