from nanohttp import json
from restfulpy.controllers import RootController, RestController, \
    JSONPatchControllerMixin

import tiger

from .member import MemberController


class Apiv1(RestController, JSONPatchControllerMixin):
    members = MemberController()

    def version(self):
        return dict(version=tiger.__version__)

    def get(self):
        return dict(get=tiger.get)

    def create(self):
        return dict(create=tiger.create)


class Root(RootController):
    apiv1 = Apiv1()

