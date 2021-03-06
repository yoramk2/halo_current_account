# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from halo_flask.flask.viewsx import AbsBaseLinkX as AbsBaseLink
from halo_flask.const import HTTPChoice
from ....mixin.mixin_view import *

class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceId(Resource,CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdMixin,AbsBaseLink):

    def get(self, cr_reference_id):

        request_vars = {}
        request_vars["cr_reference_id"] = cr_reference_id

        ret = self.do_process(request, HTTPChoice.get,request_vars)
        return ret.payload, ret.code, ret.headers

    def delete(self, cr_reference_id):

        request_vars = {}
        request_vars["cr_reference_id"] = cr_reference_id

        ret = self.do_process(request, HTTPChoice.delete,request_vars)
        return ret.payload, ret.code, ret.headers