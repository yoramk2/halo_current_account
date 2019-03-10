#!/usr/bin/env python
import logging
import urllib
import uuid
import requests
import datetime
import json
import traceback
# aws
from botocore.exceptions import ClientError
# halolib
from halo_flask.flask.viewsx import AbsBaseLinkX as AbsBaseLink
from halo_flask.flask.utilx import Util, strx
from halo_flask.ses import send_mail
from halo_flask.const import HTTPChoice
from halo_flask.events import AbsBaseHandler,AbsMainHandler
from halo_flask.exceptions import HaloException,ApiError
from halo_flask.logs import log_json
from ..views import *
from ..events import *
from halo_flask.settingsx import settingsx
settings = settingsx()

logger = logging.getLogger(__name__)

class HandlerMixin(AbsMainHandler):
	pass

