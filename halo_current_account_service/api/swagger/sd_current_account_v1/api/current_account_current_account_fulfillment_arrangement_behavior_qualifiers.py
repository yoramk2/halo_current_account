# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from halo_flask.flask.viewsx import AbsBaseLinkX as AbsBaseLink
from halo_flask.const import HTTPChoice
from ....mixin.mixin_view import *

class CurrentAccountCurrentAccountFulfillmentArrangementBehaviorQualifiers(Resource,CurrentAccountCurrentAccountFulfillmentArrangementBehaviorQualifiersMixin,AbsBaseLink):

    def get(self):

        request_vars = {}

        ret = self.do_process(request, HTTPChoice.get,request_vars)
        return ret.payload, ret.code, ret.headers