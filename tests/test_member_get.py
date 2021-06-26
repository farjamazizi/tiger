from bddrest import status, response

from tiger.models.member import Member
from tests.helpers import LocalApplicationTestCase


class TestMember(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        session = cls.create_session()

        cls.member = Member(
            user_name = 'username 2',
            first_name = 'firstname 2',
            last_name = 'lastname 2',
            birth_date='1999-05-10',
            password = 'Abc111222',
            status = 'active',
        )
        session.add(cls.member)
        session.commit()

    def test_get(self):
        with self.given(
            'get member',
            f'/apiv1/members/id:{self.member.id}',
            'GET',
        ):
            assert status == 200
            assert response.json['id'] == self.member.id
            assert response.json['userName'] == self.member.user_name
            assert response.json['firstName'] == self.member.first_name
            assert response.json['lastName'] == self.member.last_name

