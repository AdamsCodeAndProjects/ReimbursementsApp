from custom_exceptions.exceptions import IncorrectLoginCredentialsException
from data_access_layer.implementation_classes.employee_imp import EmployeeDAOImp
from entities.employee import Employee
from service_layer.abstract_service.employee_service import EmployeeService


class EmployeeImpService(EmployeeService):
    def __init__(self, employee_dao: EmployeeDAOImp):
        self.employee_dao = employee_dao

    def employee_login_request(self, employee_id: int, pass_word: str):
        validation = self.employee_dao.employee_login_request(employee_id, pass_word)
        if type(validation) == tuple:
            return True
        else:
            raise IncorrectLoginCredentialsException("Incorrect login values")
