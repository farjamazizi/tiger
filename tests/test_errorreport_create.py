from bddrest import status, response, when, given

from tests.helpers import LocalApplicationTestCase


class TestMember(LocalApplicationTestCase):

    def test_create(self):
        curl = 'http://abcd-abcdef.com/apiv1/'
        stack_trace = '{"StackTrace":"Traceback(abcd)\local'
        organization_id = '10'
        created_at = '2000-02-11'
        modified_at = '2001-02-11'
        member_id = '1'


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

