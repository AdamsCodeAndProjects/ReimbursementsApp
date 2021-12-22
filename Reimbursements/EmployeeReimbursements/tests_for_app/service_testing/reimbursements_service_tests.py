from custom_exceptions.exceptions import ReimburseNegativeAmountException, TooMuchMoneyException, \
    MustBeNumberValueException
from data_access_layer.abstract_layer.reimbursements_dao import ReimbursementsDAO
from data_access_layer.implementation_classes.reimbursements_imp import ReimbursementsImp
from entities.reimburesements import Reimbursements
from service_layer.implementation_services.reimbursements_service_imp import ReimbursementServiceImp

reim_dao = ReimbursementsImp()
reim_service = ReimbursementServiceImp(reim_dao)
new_negative_request = Reimbursements(7, 2, -350, 'Dog bite Hospital visit', 'pending', 'none', '2021-12-11')
new_million_request = Reimbursements(7, 2, 1000000, 'Dog bite Hospital visit', 'pending', 'none', '2021-12-11')
new_string_request = Reimbursements(7, 2, "1000000", 'Dog bite Hospital visit', 'pending', 'none', '2021-12-11')


def test_create_reimbursement_request_negative_value():
    try:
        reim_service.service_create_reimbursement_request(new_negative_request)
        assert False
    except ReimburseNegativeAmountException as e:
        assert str(e) == "You cannot request negative amounts"


def test_create_reimbursement_request():
    try:
        reim_service.service_create_reimbursement_request(new_million_request)
        assert False
    except TooMuchMoneyException as e:
        assert str(e) == "You cannot request this much over this app"


def test_create_for_strings():
    try:
        reim_service.service_create_reimbursement_request(new_string_request)
        assert False
    except MustBeNumberValueException as e:
        assert str(e) == "You must type in a number value"
