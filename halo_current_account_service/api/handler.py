# the views for project
# python
import datetime
import json
import logging
import urllib
import uuid
#from cStringIO import StringIO
# aws
import requests
from botocore.exceptions import ClientError
from halo_flask.ses import send_mail
# common
from halo_flask.views import AbsBaseLink
from halo_flask.util import Util, strx

from halo_current_account_service.api.mixin.mixin_handler import *

logger = logging.getLogger(__name__)

	
class HaloHandler(HandlerMixin):
	pass
	
		



