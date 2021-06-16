from bddrest import status, response, when, given

from tests.helpers import LocalApplicationTestCase


class TestMember(LocalApplicationTestCase):

    def test_create(self):
        user_name = 'farazi'
        first_name = 'farjam'
        last_name = 'azizi'
        birth_date = '1996-05-10'

        with self.given(
            'Create a member',
            '/apiv1/members'
            'CREATE',
            json=dict(
                userName=user_name,
                firstName=first_name,
                lastName=last_name,
                birthDate=birth_date
            ),
        ):
            assert status == 200
            assert response.json['id'] is not None
            assert response.json['userName'] == user_name
            assert response.json['firstName'] == first_name
            assert response.json['lastName'] == last_name
            assert response.json['birthDate'] == birth_date

            when('Trying to pass without form parameters', json={})
            assert status == '400 No Parameter Exists In The Form'

            when(
                'Trying to pass null username',
                json=given | dict(userName=None),
            )
            assert status == '400 Username is null'

            when('Trying to pass empty username', json=given - 'userName')
            assert status == '400 username is required'

            when(
                'Trying to pass less than 3 character',
                json=given | dict(userName='ab'),
            )
            assert status == '400 Username Length Must Be Greater Than 3 ' \
                             'Characters and Less than 15 Character'

            when(
                'Trying to pass greater than 15 character',
                json=given | dict(userName='a' * 20),
            )
            assert status == '400 Username Length Must Be Greater Than 3 ' \
                             'Characters and Less than 15 Character'

            when(
                'Trying to pass null firstname',
                json=given | dict(firstName=None),
            )
            assert status == '400 Firstname field is null'

            when(
                'Trying to pass null lastname',
                json=given | dict(lastName=None),
            )
            assert status == '400 Lastname field is null'

