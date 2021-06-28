from nanohttp import json, validate, context, int_or_notfound, HTTPNotFound
from restfulpy.controllers import ModelRestController
from restfulpy.orm import commit, DBSession

from tiger.models import ErrorReport
from ..exceptions import *


class ErrorReportController(ModelRestController):

    @json(prevent_empty_form=StatusEmptyForm)
    @validate(
        curl=dict(
            required=StatusCurlIsRequired,
            not_none=StatusCurlIsNull,
        ),
        stackTrace=dict(
            required=StatusStackTraceIsRequired,
            not_none=StatusStackTraceIsNull,
        ),
        status=dict(
            required=StatusReportStatusIsRequired,
            not_none=StatusReportStatusIsNull,

        ),
    )
    @commit
    def create(self):

        error_report = ErrorReport()
        error_report.update_from_request()
        DBSession.add(error_report)
        return error_report

