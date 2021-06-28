from bddrest import status, response, given

from tiger.models.member import Member
from tests.helpers import LocalApplicationTestCase


class TestMember(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        session = cls.create_session()

        cls.member = Member(
            user_name='username 2',
            first_name='firstname 2',
            last_name='lastname 2',
            birth_date='1999-05-10',
            password='Abc111222',
            status='active',
        )
        session.add(cls.member)
        session.commit()

    def test_create(self):
        curl = 'http://abcd-abcdef.com/apiv1/'
        stack_trace = '{"StackTrace":"Traceback(abcd)\local'
        organization_id = '10'
        created_at = '2000-02-11'
        modified_at = '2001-02-11'
        member_id = 'member.id'


        with self.given(
            'Create a errorreport',
            '/apiv1/errorreports',
            'CREATE',
            json=dict(
                curl=curl,
                stackTrace=stack_trace,
                organizationId=organization_id,
                createdAt=created_at,
                modifiedAt=modified_at,
                memberId=member_id,
                status='500'
            ),
        ):
            assert status == 200
            assert response.json['id'] is not None
            assert response.json['curl'] == curl
            assert response.json['stackTrace'] == stack_trace
            assert response.json['organizationId'] == organization_id
            assert response.json['createdAt'] == created_at
            assert response.json['modifiedAt'] == modified_at
            assert response.json['status'] == 'status'
            assert response.json['memberId'] == member_id

