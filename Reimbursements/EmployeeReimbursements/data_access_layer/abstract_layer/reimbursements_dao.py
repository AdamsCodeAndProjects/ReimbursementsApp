from abc import ABC, abstractmethod
from typing import List

from entities.reimburesements import Reimbursements


class ReimbursementsDAO(ABC):

    @abstractmethod
    def create_reimbursement_request(self, reimburse: Reimbursements) -> Reimbursements:
        pass

    @abstractmethod
    def reimbursement_request_approval(self, approval: str, transaction_id: int, ) -> bool:
        pass

    @abstractmethod
    def comment_about_reimbursement_request(self, manager_comment: str, transaction_id: int)-> Reimbursements:
        pass

    @abstractmethod
    def view_pending_reimbursement_requests(self) -> List[Reimbursements]:
        pass

    @abstractmethod
    def view_past_reimbursement_requests(self) -> List[Reimbursements]:
        pass

    @abstractmethod
    def view_reimbursement_statistics_one(self, employee_id: int):
        pass

    @abstractmethod
    def view_reimbursement_statistics_two(self, employee_id: int):
        pass

    @abstractmethod
    def view_reimbursement_statistics_three(self, employee_id: int):
        pass

    @abstractmethod
    def view_reimbursement_statistics_four(self, employee_id: int):
        pass

    @abstractmethod
    def view_reimbursement_statistics_five(self, employee_id: int):
        pass

    @abstractmethod
    def review_reimbursement_request(self, employee_id: int) -> List[Reimbursements]:
        pass

    @abstractmethod
    def get_reimbursement_by_id(self, transaction_id: int) -> Reimbursements:
        pass


