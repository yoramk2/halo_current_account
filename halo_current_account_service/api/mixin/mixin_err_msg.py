#!/usr/bin/env python
import logging
import urllib
import uuid
import datetime
import json
# aws
from botocore.exceptions import ClientError
# common
from halo_flask.const import HTTPChoice
from halo_flask.exceptions import HaloException
from halo_bian.bian.mixin_err_msg import ErrorMessages



logger = logging.getLogger(__name__)


class ErrorMessages(ErrorMessages):

    #custom messages
    ErrorMessages.hashx["MaxTryException"] = { "code" : 123, "message" : "Server Error" }




