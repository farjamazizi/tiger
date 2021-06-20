from nanohttp import HTTPKnownStatus


class StatusInvalidStringType(HTTPKnownStatus):
    status = '400 Invalid Type For Username'


class StatusUsernameLengthInvalid(HTTPKnownStatus):
    status = '400 Username Length Must Be Greater Than 3' \
             ' Characters And Less Than 15 Character'


class StatusUsernameIsRequired(HTTPKnownStatus):
    status = '400 Username Is Required'


class StatusUsernameIsNull(HTTPKnownStatus):
    status = '400 Username Is Null'


class StatusFirstnameIsNull(HTTPKnownStatus):
    status = '400 Firstname Field Is Null'


class StatusLastnameIsNull(HTTPKnownStatus):
    status = '400 Lastname Field Is Null'


class HttpPasswordNotInForm(HTTPKnownStatus):
    status = '400 Password Not In Form'


class HttpPasswordIsNull(HTTPKnownStatus):
    status = '400 Password Is Null'


class HttpPasswordInvalidLength(HTTPKnownStatus):
    status = '400 Invalid Password Length'


class HttpPasswordWrongPattern(HTTPKnownStatus):
    status = '400 Password Not Complex Enough'


class StatusRepetitiveUsername(HTTPKnownStatus):
    status = '400 Username Is Already Exist'


class StatusPreventEmptyForm(HTTPKnownStatus):
    status = '400 No Parameter Exists In The Form'

