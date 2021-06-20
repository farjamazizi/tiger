from nanohttp import HTTPKnownStatus, settings


class StatusInvalidStringType(HTTPKnownStatus):
    status = '400 INVALID TYPE FOR USERNAME'


class StatusUsernameLengthInvalid(HTTPKnownStatus):
    status = '400 USERNAME LENGTH MUST BE GREATER THAN 3' \
             ' CHARACTERS AND LESS THAN 15 CHARACTER'


class StatusUsernameIsRequired(HTTPKnownStatus):
    status = '400 USERNAME IS REQUIRED'


class StatusUsernameIsNull(HTTPKnownStatus):
    status = '400 USERNAME IS NULL'


class StatusFirstnameIsNull(HTTPKnownStatus):
    status = '400 FIRSTNAME FIELD IS NULL'


class StatusLastnameIsNull(HTTPKnownStatus):
    status = '400 LASTNAME FIELD IS NULL'


class StatusRepetitiveUsername(HTTPKnownStatus):
    status = '400 USERNAME IS ALREADY EXIST'


class HTTPPasswordNotInForm(HTTPKnownStatus):
    status = '400 PASSWORD NOT IN FORM'


class HTTPPasswordIsNull(HTTPKnownStatus):
    status = '400 PASSWORD IS NULL'


class HTTPPasswordInvalidLength(HTTPKnownStatus):
    status = '400 INVALID PASSWORD LENGTH'


class HTTPPasswordWrongPattern(HTTPKnownStatus):
    status = '400 PASSWORD NOT COMPLEX ENOUGH'


class StatusPreventEmptyForm(HTTPKnownStatus):
    status = '400 NO PARAMETER EXISTS IN THE FORM'

