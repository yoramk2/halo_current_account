#!/usr/bin/env python
import logging
import urllib
import uuid
import datetime
import json
from requests import *
# aws
from botocore.exceptions import ClientError
# common
from halo_flask.flask.utilx import Util, strx
from halo_flask.const import HTTPChoice
from halo_flask.flask.mixinx import AbsBaseMixinX as AbsBaseMixin
from halo_flask.exceptions import HaloException,ApiError,BadRequestError
from halo_flask.ses import send_mail
from halo_flask.logs import log_json
from halo_flask.flask.viewsx import AbsBaseLinkX as AbsBaseLink
from halo_flask.response import HaloResponse
# flask
from flask import Response as HttpResponse


from ..dbutil import *
from ..apis import *
from ..events import *
from halo_flask.settingsx import settingsx
settings = settingsx()

logger = logging.getLogger(__name__)

#@TODO 1. all proprietery code goes to mixin
#@TODO 2. add settings params to extend
#@TODO 3. add settings param data to .env
#@TODO 4. populate static dir
#@TODO 5. populate templates dir
#@TODO 6. add tests

dbaccess = None
def get_dbaccess(req_context):
    global dbaccess
    if dbaccess is None:
        dbaccess = DbUtil(req_context)
    return dbaccess

def get_event_dbaccess():
    req_context = Util.event_req_context
    dbaccess = DbUtil(req_context)
    return dbaccess

def bad_request_view(request):
    logger.debug('system-error 400')
    return HttpResponse(status=400)

def permission_denied_view(request):
    logger.error('system-error 403')
    return HttpResponse(status=403)

def page_not_found_view(request):
    logger.error('system-error 404')
    return HttpResponse(status=404)

def error_view(request):
    logger.error('system-error 500')
    return HttpResponse(status=500)




from halo_bian.bian.abs_bian_srv import AbsBianMixin


class CurrentAccountCurrentAccountFulfillmentArrangementMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementBehaviorQualifiersMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdBehaviorQualifierMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdDepositsBqReferenceIdMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdStandingOrdersBqReferenceIdMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdDirectDebitsBqReferenceIdMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdSweepsBqReferenceIdMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdInventoriesBqReferenceIdMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdLiensBqReferenceIdMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdInterestsBqReferenceIdMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdFeesBqReferenceIdMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdStatementsBqReferenceIdMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdReportsBqReferenceIdMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementInitiationMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdUpdationMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdRecordingMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdDepositsBqReferenceIdExecutionMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdDepositsExecutionMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdExecutionMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsExecutionMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdStandingOrdersBqReferenceIdRequisitionMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdStandingOrdersRequisitionMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdDirectDebitsBqReferenceIdRequisitionMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdDirectDebitsRequisitionMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdSweepsBqReferenceIdRequisitionMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdSweepsRequisitionMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdInventoriesBqReferenceIdRequisitionMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdInventoriesRequisitionMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdLiensBqReferenceIdRequisitionMixin(AbsBianMixin):
	pass
class CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdLiensRequisitionMixin(AbsBianMixin):
	pass

