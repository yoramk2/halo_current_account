# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from halo_flask.flask.viewsx import AbsBaseLinkX as AbsBaseLink
from halo_flask.const import HTTPChoice
from ....mixin.mixin_view import *

class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdSweepsBqReferenceIdRequisition(Resource,CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdSweepsBqReferenceIdRequisitionMixin,AbsBaseLink):

    def put(self, cr_reference_id, bq_reference_id):
        print(g.json)

        request_vars = {}
        request_vars["cr_reference_id"] = cr_reference_id
        request_vars["bq_reference_id"] = bq_reference_id

        ret = self.do_process(request, HTTPChoice.put,request_vars)
        return ret.payload, ret.code, ret.headers