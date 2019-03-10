# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.current_account_current_account_fulfillment_arrangement import CurrentAccountCurrentAccountFulfillmentArrangement
from .api.current_account_current_account_fulfillment_arrangement_behavior_qualifiers import CurrentAccountCurrentAccountFulfillmentArrangementBehaviorQualifiers
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_behavior_qualifier import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdBehaviorQualifier
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceId
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_deposits_bq_reference_id import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdDepositsBqReferenceId
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_payments_bq_reference_id import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceId
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_standing_orders_bq_reference_id import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdStandingOrdersBqReferenceId
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_direct_debits_bq_reference_id import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdDirectDebitsBqReferenceId
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_sweeps_bq_reference_id import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdSweepsBqReferenceId
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_inventories_bq_reference_id import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdInventoriesBqReferenceId
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_liens_bq_reference_id import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdLiensBqReferenceId
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_interests_bq_reference_id import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdInterestsBqReferenceId
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_fees_bq_reference_id import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdFeesBqReferenceId
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_statements_bq_reference_id import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdStatementsBqReferenceId
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_reports_bq_reference_id import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdReportsBqReferenceId
from .api.current_account_current_account_fulfillment_arrangement_initiation import CurrentAccountCurrentAccountFulfillmentArrangementInitiation
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_updation import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdUpdation
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_recording import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdRecording
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_deposits_bq_reference_id_execution import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdDepositsBqReferenceIdExecution
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_deposits_execution import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdDepositsExecution
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_payments_bq_reference_id_execution import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdExecution
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_payments_execution import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsExecution
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_standing_orders_bq_reference_id_requisition import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdStandingOrdersBqReferenceIdRequisition
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_standing_orders_requisition import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdStandingOrdersRequisition
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_direct_debits_bq_reference_id_requisition import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdDirectDebitsBqReferenceIdRequisition
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_direct_debits_requisition import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdDirectDebitsRequisition
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_sweeps_bq_reference_id_requisition import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdSweepsBqReferenceIdRequisition
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_sweeps_requisition import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdSweepsRequisition
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_inventories_bq_reference_id_requisition import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdInventoriesBqReferenceIdRequisition
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_inventories_requisition import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdInventoriesRequisition
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_liens_bq_reference_id_requisition import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdLiensBqReferenceIdRequisition
from .api.current_account_current_account_fulfillment_arrangement_cr_reference_id_liens_requisition import CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdLiensRequisition


routes = [
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangement, urls=['/current-account/current-account-fulfillment-arrangement'], endpoint='current_account_current_account_fulfillment_arrangement'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementBehaviorQualifiers, urls=['/current-account/current-account-fulfillment-arrangement/behavior-qualifiers'], endpoint='current_account_current_account_fulfillment_arrangement_behavior_qualifiers'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdBehaviorQualifier, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/<behavior_qualifier>'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_behavior_qualifier'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceId, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdDepositsBqReferenceId, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/deposits/<bq_reference_id>'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_deposits_bq_reference_id'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceId, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/payments/<bq_reference_id>'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_payments_bq_reference_id'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdStandingOrdersBqReferenceId, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/standing-orders/<bq_reference_id>'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_standing_orders_bq_reference_id'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdDirectDebitsBqReferenceId, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/direct-debits/<bq_reference_id>'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_direct_debits_bq_reference_id'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdSweepsBqReferenceId, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/sweeps/<bq_reference_id>'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_sweeps_bq_reference_id'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdInventoriesBqReferenceId, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/inventories/<bq_reference_id>'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_inventories_bq_reference_id'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdLiensBqReferenceId, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/liens/<bq_reference_id>'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_liens_bq_reference_id'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdInterestsBqReferenceId, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/interests/<bq_reference_id>'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_interests_bq_reference_id'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdFeesBqReferenceId, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/fees/<bq_reference_id>'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_fees_bq_reference_id'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdStatementsBqReferenceId, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/statements/<bq_reference_id>'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_statements_bq_reference_id'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdReportsBqReferenceId, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/reports/<bq_reference_id>'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_reports_bq_reference_id'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementInitiation, urls=['/current-account/current-account-fulfillment-arrangement/initiation'], endpoint='current_account_current_account_fulfillment_arrangement_initiation'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdUpdation, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/updation'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_updation'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdRecording, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/recording'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_recording'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdDepositsBqReferenceIdExecution, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/deposits/<bq_reference_id>/execution'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_deposits_bq_reference_id_execution'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdDepositsExecution, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/deposits/execution'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_deposits_execution'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdExecution, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/payments/<bq_reference_id>/execution'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_payments_bq_reference_id_execution'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsExecution, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/payments/execution'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_payments_execution'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdStandingOrdersBqReferenceIdRequisition, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/standing-orders/<bq_reference_id>/requisition'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_standing_orders_bq_reference_id_requisition'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdStandingOrdersRequisition, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/standing-orders/requisition'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_standing_orders_requisition'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdDirectDebitsBqReferenceIdRequisition, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/direct-debits/<bq_reference_id>/requisition'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_direct_debits_bq_reference_id_requisition'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdDirectDebitsRequisition, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/direct-debits/requisition'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_direct_debits_requisition'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdSweepsBqReferenceIdRequisition, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/sweeps/<bq_reference_id>/requisition'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_sweeps_bq_reference_id_requisition'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdSweepsRequisition, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/sweeps/requisition'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_sweeps_requisition'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdInventoriesBqReferenceIdRequisition, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/inventories/<bq_reference_id>/requisition'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_inventories_bq_reference_id_requisition'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdInventoriesRequisition, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/inventories/requisition'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_inventories_requisition'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdLiensBqReferenceIdRequisition, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/liens/<bq_reference_id>/requisition'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_liens_bq_reference_id_requisition'),
    dict(resource=CurrentAccountCurrentAccountFulfillmentArrangementCrReferenceIdLiensRequisition, urls=['/current-account/current-account-fulfillment-arrangement/<cr_reference_id>/liens/requisition'], endpoint='current_account_current_account_fulfillment_arrangement_cr_reference_id_liens_requisition'),
]