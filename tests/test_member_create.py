from bddrest import status, response, when, given

from tests.helpers import LocalApplicationTestCase


class TestMember(LocalApplicationTestCase):

    def test_create(self):
        user_name = 'username 1'
        first_name = 'firstname 1'
        last_name = 'lastname 1'
        birth_date = '1996-05-10'
        password = 'Far13751375'
        email = 'Farjamazizi@gmail.com'

        with self.given(
            'Create a member',
            '/apiv1/members',
            'CREATE',
            json=dict(
                userName=user_name,
                firstName=first_name,
                lastName=last_name,
                birthDate=birth_date,
                password=password,
                status='active',
                email=email
            ),
        ):
            assert status == 200
            assert response.json['id'] is not None
            assert response.json['userName'] == user_name
            assert response.json['firstName'] == first_name
            assert response.json['lastName'] == last_name
            assert response.json['birthDate'] == birth_date
            assert response.json['status'] == 'active'
            assert response.json['email'] == email

            when('Trying to pass without form parameters', json={})
            assert status == '400 Empty Form'

            when(
                'Trying to pass null username',
                json=given | dict(userName=None),
            )
            assert status == '400 Username Is Null'

            when('Trying to pass empty username', json=given - 'userName')
            assert status == '400 Username Is Required'

            when(
                'Trying to pass less than 3 character',
                json=given | dict(userName='ab'),
            )
            assert status == '400 Username Length Must Be Greater Than 3 ' \
                             'Characters And Less Than 15 Character'

            when(
                'Trying to pass greater than 20 character',
                json=given | dict(userName='a' * 20),
            )
            assert status == '400 Username Length Must Be Greater Than 3 ' \
                             'Characters And Less Than 15 Character'

            when(
                'Trying to pass null firstname',
                json=given | dict(firstName=None),
            )
            assert status == '400 Firstname Field Is Null'

            when(
                'Trying to pass null lastname',
                json=given | dict(lastName=None),
            )
            assert status == '400 Lastname Field Is Null'

            when(
                'Trying to pass null member status',
                json=given | dict(status=None, userName='username2',),
            )
            assert status == '400 Status Is null'

            when('Trying to pass empty MemberStatus', json=given - 'status')
            assert status == '400 MemberStatus is Required'

            when('Trying to pass null email', json=given | dict(email=None))
            assert status == '400 Email Is Null'

            when('Trying to pass empty email', json=given - 'email')
            assert status == '400 Email Not In Form'

