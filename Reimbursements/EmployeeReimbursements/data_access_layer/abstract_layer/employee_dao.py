from abc import ABC, abstractmethod
from typing import List

from entities.employee import Employee
from entities.reimburesements import Reimbursements


class EmployeeDAO(ABC):

    @abstractmethod
    def employee_login_request(self, employee_id: int, pass_word: str) -> bool:
        pass
