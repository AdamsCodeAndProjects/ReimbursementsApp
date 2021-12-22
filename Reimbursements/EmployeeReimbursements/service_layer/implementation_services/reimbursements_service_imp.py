# from abc import ABC
from typing import List

from custom_exceptions.exceptions import ReimburseNegativeAmountException, TooMuchMoneyException, \
    NegativeTransactionIdException, MustBeNumberValueException
from data_access_layer.implementation_classes.reimbursements_imp import ReimbursementsImp
from entities.reimburesements import Reimbursements
from service_layer.abstract_service.reimbursement_service import ReimbursementService


class ReimbursementServiceImp(ReimbursementService):
    def __init__(self, reimbursements_dao: ReimbursementsImp):
        self.reimbursements_dao = reimbursements_dao

    def service_create_reimbursement_request(self, reimburse: Reimbursements) -> Reimbursements:
        if type(reimburse.reimbursement_amount) != int:
            raise MustBeNumberValueException("You must type in a number value")
        if reimburse.reimbursement_amount < 0:
            raise ReimburseNegativeAmountException("You cannot request negative amounts")
        if reimburse.reimbursement_amount > 10000:
            raise TooMuchMoneyException("You cannot request this much over this app")
        new_account = self.reimbursements_dao.create_reimbursement_request(reimburse)
        return new_account

    def service_reimbursement_request_approval(self, transaction_id: int, approval: str) -> Reimbursements:
        return self.reimbursements_dao.reimbursement_request_approval(approval, transaction_id)

    def service_comment_about_reimbursement_request(self, manager_comment: str, transaction_id: int) -> Reimbursements:
        return self.reimbursements_dao.comment_about_reimbursement_request(manager_comment, transaction_id)

    def service_view_pending_reimbursement_requests(self) -> List[Reimbursements]:
        return self.reimbursements_dao.view_pending_reimbursement_requests()

    def service_view_past_reimbursement_requests(self) -> List[Reimbursements]:
        return self.reimbursements_dao.view_past_reimbursement_requests()

    def service_view_reimbursement_statistics_one(self, employee_id: int):
        return self.reimbursements_dao.view_reimbursement_statistics_one(employee_id)

    def service_view_reimbursement_statistics_two(self, employee_id: int):
        return self.reimbursements_dao.view_reimbursement_statistics_two(employee_id)

    def service_view_reimbursement_statistics_three(self, employee_id: int):
        return self.reimbursements_dao.view_reimbursement_statistics_three(employee_id)

    def service_view_reimbursement_statistics_four(self, employee_id: int):
        return self.reimbursements_dao.view_reimbursement_statistics_four(employee_id)

    def service_view_reimbursement_statistics_five(self, employee_id: int):
        return self.reimbursements_dao.view_reimbursement_statistics_five(employee_id)

    def service_review_reimbursement_request(self, employee_id: int) -> List[Reimbursements]:
        return self.reimbursements_dao.review_reimbursement_request(employee_id)

    def service_get_reimbursement_by_id(self, employee_id: int) -> Reimbursements:
        return self.reimbursements_dao.get_reimbursement_by_id(employee_id)







