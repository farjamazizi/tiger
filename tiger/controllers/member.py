from nanohttp import json, validate, context, int_or_notfound, HTTPNotFound
from restfulpy.controllers import ModelRestController
from restfulpy.orm import commit, DBSession

from tiger.models import Member
from ..exceptions import *


class MemberController(ModelRestController):

    @json(
        prevent_empty_form='400 No Parameter Exists In The Form',
    )
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
    )
    @commit
    def create(self):
        member_username_check = DBSession.query(Member) \
              .filter(Member.user_name == context.form.get('userName')) \
              .one_or_none()
        if member_username_check is not None:
            raise StatusRepetitiveUsername()

        member = Member()
        member.update_form_request()
        DBSession.add(member)
        return member
    @json
    def get(self, id):
        id = int_or_notfound(id)
        member = DBSession.query(Member).get(id)
        if member is None:
            raise HTTPNotFound()
        return member



