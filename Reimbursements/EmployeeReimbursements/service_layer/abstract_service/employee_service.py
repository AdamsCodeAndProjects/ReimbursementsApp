from abc import abstractmethod, ABC

from entities.employee import Employee


class EmployeeService(ABC):

    @abstractmethod
    def employee_login_request(self, employee_id: int, pass_word: str) -> bool:
        pass


