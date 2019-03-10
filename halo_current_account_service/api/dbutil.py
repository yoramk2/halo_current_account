
import logging
import datetime
from datetime import timedelta
import json
import uuid


from pynamodb.models import Model
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
from pynamodb.attributes import UnicodeAttribute,NumberAttribute,BooleanAttribute, UTCDateTimeAttribute
from pynamodb.exceptions import DoesNotExist,QueryError,PynamoDBException

from halo_flask.exceptions import HaloError
from halo_flask.logs import log_json
# mixin
from .mixin.mixin_db import *
from .models import *

#java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb -port 8600

logger = logging.getLogger(__name__)

tbl = False


class DbUtil(DbMixin):

	def __init__(self, req_context):
		super(DbUtil, self).__init__(req_context)
		try:
			logger.debug('start db setup')
			self.setup()
			logger.debug('finish db setup')
		except PynamoDBException as e:
			logger.error(str(e), extra=log_json(req_context))
			raise HaloError("error in db setup:"+str(e))

	def setup(self):
		global tbl
		tbl = True


		            

