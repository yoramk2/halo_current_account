#!/usr/bin/env python
import os
import logging
import datetime
import uuid
from pynamodb.exceptions import DoesNotExist,QueryError,PynamoDBException
from halo_flask.exceptions import HaloException
from halo_flask.flask.utilx import strx
from halo_flask.models import AbsDbMixin
from ..models import *
from halo_flask.logs import log_json
from halo_flask.settingsx import settingsx
settings = settingsx()

logger = logging.getLogger(__name__)


class DbMixin(AbsDbMixin):
	pass


