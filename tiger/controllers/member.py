import re

from nanohttp import json, validate, context, int_or_notfound, HTTPNotFound
from restfulpy.controllers import ModelRestController
from restfulpy.orm import commit, DBSession

from tiger.models import Member
from ..exceptions import *


MEMBER_PASSWORD_PATTERN = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).+')


class MemberController(ModelRestController):

    @json(prevent_empty_form=StatusEmptyForm)
    @validate(
        userName=dict(
            type_=(str, StatusInvalidStringType),
            min_length=(3, StatusUsernameLengthInvalid),
            max_length=(15, StatusUsernameLengthInvalid),
            required=StatusUsernameIsRequired,
            not_none=StatusUsernameIsNull,
        ),
        firstName=dict(
            not_none=StatusFirstnameIsNull,
        ),
        lastName=dict(
            not_none=StatusLastnameIsNull,
        ),
        password=dict(
            required=StatusPasswordNotInForm,
            not_none=StatusPasswordIsNull,
            min_length=(3, StatusPasswordInvalidLength),
            max_length=(15, StatusPasswordInvalidLength),
            pattern=(MEMBER_PASSWORD_PATTERN, StatusPasswordWrongPattern),
        ),
        status=dict(
            not_none=StatusMemberStatusIsNull,
            required=StatusMemberStatusRequired,
        ),
    )
    @commit
    def create(self):
        member_username_check = DBSession.query(Member) \
            .filter(Member.user_name == context.form.get('userName')) \
            .one_or_none()
        if member_username_check is not None:
            raise StatusRepetitiveUsername()

        member = Member()
        member.update_from_request()
        DBSession.add(member)
        return member

    @json
    def get(self, id):
        id = int_or_notfound(id)
        member = DBSession.query(Member).get(id)
        if member is None:
            raise HTTPNotFound()
        return member

