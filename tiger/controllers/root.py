from nanohttp import json
from restfulpy.controllers import RootController, RestController, \
    JSONPatchControllerMixin

import tiger

from .member import MemberController


class Apiv1(RestController, JSONPatchControllerMixin):
    members = MemberController()


    @json
    def version(self):
        return dict(version=tiger.__version__)


class Root(RootController):
    apiv1 = Apiv1()

