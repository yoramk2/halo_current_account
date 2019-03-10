# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from halo_flask.flask.viewsx import AbsBaseLinkX as AbsBaseLink
from halo_flask.const import HTTPChoice
from ....mixin.mixin_view import *

class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdBehaviorQualifier(Resource,CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdBehaviorQualifierMixin,AbsBaseLink):

    def get(self, cr_reference_id, behavior_qualifier):
        print(g.args)

        request_vars = {}
        request_vars["cr_reference_id"] = cr_reference_id
        request_vars["behavior_qualifier"] = behavior_qualifier

        ret = self.do_process(request, HTTPChoice.get,request_vars)
        return ret.payload, ret.code, ret.headers