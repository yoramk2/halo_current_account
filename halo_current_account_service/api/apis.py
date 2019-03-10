# the views for project
# python
import os
import datetime
import json
import logging
import urllib
import uuid
import requests
# aws
from botocore.exceptions import ClientError
# common
from halo_flask.const import HTTPChoice
from halo_flask.apis import AbsBaseApi
# django

# DRF


logger = logging.getLogger(__name__)



class RecaptchaApi(AbsBaseApi):
	name = 'Recaptcha'


