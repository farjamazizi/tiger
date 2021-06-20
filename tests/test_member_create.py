from bddrest import status, response, when, given

from tests.helpers import LocalApplicationTestCase


class TestMember(LocalApplicationTestCase):

    def test_create(self):
        user_name = 'username 1'
        first_name = 'firstname 1'
        last_name = 'lastname 1'
        birth_date = '1996-05-10'
        password='Far13751375'

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
            ),
        ):
            assert status == 200
            assert response.json['id'] is not None
            assert response.json['userName'] == user_name
            assert response.json['firstName'] == first_name
            assert response.json['lastName'] == last_name
            assert response.json['birthDate'] == birth_date

            when(
                'TRYING TO PASS NULL USERNAME',
                json=given | dict(userName=None),
            )
            assert status == '400 USERNAME IS NULL'

            when('TRYING TO PASS EMPTY USERNAME', json=given - 'userName')
            assert status == '400 USERNAME IS REQUIRED'

            when(
                'TRYING TO PASS LESS THAN 3 CHARACTER',
                json=given | dict(userName='AB'),
            )
            assert status == '400 USERNAME LENGTH MUST BE GREATER THAN 3 ' \
                             'CHARACTERS AND LESS THAN 15 CHARACTER'

            when(
                'TRYING TO PASS GREATER THAN 15 CHARACTER',
                json=given | dict(userName='A' * 20),
            )
            assert status == '400 USERNAME LENGTH MUST BE GREATER THAN 3 ' \
                             'CHARACTERS AND LESS THAN 15 CHARACTER'

            when(
                'Trying to pass null firstname',
                json=given | dict(firstName=None),
            )
            assert status == '400 FIRSTNAME FIELD IS NULL'

            when(
                'Trying to pass null lastname',
                json=given | dict(lastName=None),
            )
            assert status == '400 LASTNAME FIELD IS NULL'

