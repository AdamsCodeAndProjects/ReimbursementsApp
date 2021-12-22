from data_access_layer.implementation_classes.employee_imp import EmployeeDAOImp
from service_layer.implementation_services.employee_service_imp import EmployeeImpService

employee_dao = EmployeeDAOImp()
employee_service = EmployeeImpService(employee_dao)

emp_id = 5
pass_words = "venom"


def test_validate_correct_credentials():
    validation = employee_service.employee_login_request(emp_id, pass_words)
    assert validation


def test_catch_bad_employee_id():
    validation = employee_service.employee_login_request(68, pass_words)
    if validation:
        assert False
    else:
        assert True


def test_catch_bad_password():
    validation = employee_service.employee_login_request(emp_id, "IDK")
    if validation:
        assert False
    else:
        assert True


def test_catch_bad_employee_id_and_password():
    validation = employee_service.employee_login_request(66006, "sajsff")
    if validation:
        assert False
    else:
        assert True
