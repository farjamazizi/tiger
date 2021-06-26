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


class StatusPasswordNotInForm(HTTPKnownStatus):
    status = '400 Password Not In Form'


class StatusPasswordIsNull(HTTPKnownStatus):
    status = '400 Password Is Null'


class StatusPasswordInvalidLength(HTTPKnownStatus):
    status = '400 Invalid Password Length'


class StatusPasswordWrongPattern(HTTPKnownStatus):
    status = '400 Password Not Complex Enough'


class StatusRepetitiveUsername(HTTPKnownStatus):
    status = '400 Username Is Already Exist'


class StatusEmptyForm(HTTPKnownStatus):
    status = '400 Empty Form'


class StatusMemberStatusIsNull(HTTPKnownStatus):
    status = '400 Status Is null'


class StatusMemberStatusRequired(HTTPKnownStatus):
    status = '400 MemberStatus is Required'

class StatusEmailIsRequired(HTTPKnownStatus):
    status = '400 Email Not In Form'


class StatusEmailIsNull(HTTPKnownStatus):
    status = '400 Email Is Null'


class StatusInvalidEmailFormat(HTTPKnownStatus):
    status = '400 Invalid Email Format'

