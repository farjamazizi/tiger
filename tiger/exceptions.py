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
    status = '400 MemberStatus Is Required'


class StatusCurlIsRequired(HTTPKnownStatus):
    status = '400 Curl Is Required'


class StatusCurlIsNull(HTTPKnownStatus):
    status = '400 Curl Is Null'


class StatusStackTraceIsRequired(HTTPKnownStatus):
    status = '400 StackTrace Is Required'


class StatusStackTraceIsNull(HTTPKnownStatus):
    status = '400 StackTrace Is Null'


class StatusReportStatusIsRequired(HTTPKnownStatus):
    status = '400 ReportStatus Is Required'

class StatusReportStatusIsNull(HTTPKnownStatus):
    status = '400 ReportStatus Is Null'


class StatusRpetitiveCurlError(HTTPKnownStatus):
    status = '400 CurlError Is Already Exist'

class StatusRpetitiveStackTrace(HTTPKnownStatus):
    status = '400 StatusError Is Already Exist'



