from nanohttp import json
from restfulpy.controllers import RootController, RestController, \
    JSONPatchControllerMixin

import tiger

from .member import MemberController
from .error_report import ErrorReportController


class Apiv1(RestController, JSONPatchControllerMixin):
    members = MemberController()
    errorreports = ErrorReportController()

    @json
    def version(self):
        return dict(version=tiger.__version__)


class Root(RootController):
    apiv1 = Apiv1()

