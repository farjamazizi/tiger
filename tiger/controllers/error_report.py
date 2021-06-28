from nanohttp import json, validate, context, int_or_notfound, HTTPNotFound
from restfulpy.controllers import ModelRestController
from restfulpy.orm import commit, DBSession

from tiger.models import ErrorReport
from ..exceptions import *


class MemberController(ModelRestController):

    @json(prevent_empty_form=StatusEmptyForm)
    @validate(
        curl=dict(
            required=StatusCurlIsRequired,
            not_none=StatusCurlIsNull,
        ),
        stack_trace=dict(
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
        errorreport_curl_check = DBSession.query(ErrorReport) \
                   .filter(ErrorReport.curl == context.form.get('curl')) \
                   .one_or_none()
        if errorreport_curl_check is not None:
            raise StatusRpetitiveCurlError

        errorreport_stacktrace_check = DBSession.query(ErrorReport) \
                   .filter(ErrorReport.status == context.form.get('status')) \
                   .one_or_none()
        if errorreport_stacktrace_check is not None:
            raise StatusRpetitiveStackTrace

