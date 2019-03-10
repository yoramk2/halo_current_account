# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required

#blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

# the views for project
# python
import datetime
import json
import logging
import urllib
import uuid
import requests
#flask
from flask import Response as HttpResponse
# aws
from botocore.exceptions import ClientError
# common
from halo_flask.flask.mixinx import PerfMixinX as PerfMixin
from halo_flask.flask.viewsx import AbsBaseLinkX as AbsBaseLink
# mixin
from .mixin.mixin_view import *
from .dbutil import DbUtil
from halo_flask.settingsx import settingsx

settings = settingsx()

logger = logging.getLogger(__name__)


          



class PerfLink(PerfMixin, AbsBaseLink):
	pass



from halo_flask.flask.mixinx import AbsBaseMixinX
from .mixin.mixin_handler import HandlerMixin


class EventLink__(AbsBaseMixinX, AbsBaseLink):
	def process_post(self, request, vars):
		event = request.data
		ctx = request.META
		handler = HandlerMixin()
		handler.get_event(event, ctx)
		return HttpResponse()