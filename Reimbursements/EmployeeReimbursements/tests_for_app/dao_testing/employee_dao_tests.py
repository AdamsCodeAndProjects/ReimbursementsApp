# from data_access_layer.abstract_layer import
from data_access_layer.abstract_layer.employee_dao import EmployeeDAO
from data_access_layer.implementation_classes.employee_imp import EmployeeDAOImp
from entities import employee
from entities.employee import Employee

employee_dao_referral = EmployeeDAOImp()
requester = Employee("Peter", "Parker", 2, "tulip", False)


def test_employee_login_request():
    validated = employee_dao_referral.employee_login_request(requester.employee_id,
                                                             requester.password)
    assert validated


def test_not_validated_login():
    validated = employee_dao_referral.employee_login_request(55, "bad")
    assert validated is None
