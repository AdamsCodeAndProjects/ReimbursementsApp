from abc import abstractmethod, ABC
from typing import List

from entities.reimburesements import Reimbursements


class ReimbursementService(ABC):

    @abstractmethod
    def service_create_reimbursement_request(self, reimburse: Reimbursements) -> Reimbursements:
        pass

    @abstractmethod
    def service_reimbursement_request_approval(self, transaction_id: int, approval: str) -> Reimbursements:
        pass

    @abstractmethod
    def service_comment_about_reimbursement_request(self, manager_comment: str, transaction_id: int) -> Reimbursements:
        pass

    @abstractmethod
    def service_view_pending_reimbursement_requests(self) -> List[Reimbursements]:
        pass

    @abstractmethod
    def service_view_past_reimbursement_requests(self) -> List[Reimbursements]:
        pass

    @abstractmethod
    def service_view_reimbursement_statistics_one(self, employee_id: int):
        pass

    @abstractmethod
    def service_view_reimbursement_statistics_two(self, employee_id: int):
        pass

    @abstractmethod
    def service_view_reimbursement_statistics_three(self, employee_id: int):
        pass

    @abstractmethod
    def service_view_reimbursement_statistics_four(self, employee_id: int):
        pass

    @abstractmethod
    def service_view_reimbursement_statistics_five(self, employee_id: int):
        pass

    @abstractmethod
    def service_review_reimbursement_request(self, employee_id: int) -> List[Reimbursements]:
        pass

    @abstractmethod
    def service_get_reimbursement_by_id(self, employee_id: int) -> Reimbursements:
        pass
