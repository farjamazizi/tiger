from bddrest import status, response, when, given

from tests.helpers import LocalApplicationTestCase


class TestMember(LocalApplicationTestCase):

    def test_create(self):
        curl = ''
        stack_trace = ''
        status = ''
        organization_id = '10'
        created_at = '2000-02-11'
        modified_at = '2001-02-11'
        member_id = '1'


        with self.given(
            'Create a member',
            '/apiv1/members',
            'CREATE',
            json=dict(
                curl=curl,
                stack_trace=stack_trace,
                organization_id=organization_id,
                created_at=created_at,
                modified_at=modified_at,
                member_id=member_id,
                status='active',
            ),
        ):
            assert status == 200
            assert response.json['id'] is not None
            assert response.json['curl'] == curl
            assert response.json['stack_trace'] == stack_trace
            assert response.json['organization_id'] == organization_id
            assert response.json['created_at'] == created_at
            assert response.json['modified_at'] == modified_at
            assert response.json['status'] == status
