from data_access_layer.abstract_layer import reimbursements_dao
from data_access_layer.abstract_layer.reimbursements_dao import ReimbursementsDAO
from data_access_layer.implementation_classes.reimbursements_imp import ReimbursementsImp
from entities.reimburesements import Reimbursements

new_request = Reimbursements(7, 2, 350, 'Dog bite Hospital visit', 'pending', 'none', '2021-12-11')
reim_dao = ReimbursementsImp()


def test_create_reimbursement_request_success():
    account_result = reim_dao.create_reimbursement_request(new_request)
    assert account_result.transaction_id > 0


def test_reimbursement_request_approval_success():
    result = reim_dao.reimbursement_request_approval("approved", 7)
    assert result.status == "approved"


def test_comment_about_reimbursement_request():
    result = reim_dao.comment_about_reimbursement_request("What is this?  Terrible!", 7)
    assert result.manager_comment == "What is this?  Terrible!"


def test_view_pending_reimbursement_requests():
    result = reim_dao.view_pending_reimbursement_requests()
    assert len(result) >= 2


def test_view_past_reimbursement_requests():
    result = reim_dao.view_pending_reimbursement_requests()
    assert len(result) >= 2


def test_view_reimbursement_statistics_one():
    result = reim_dao.view_reimbursement_statistics_one(2)
    assert result >= 10


def test_view_reimbursement_statistics_two():
    result = reim_dao.view_reimbursement_statistics_two(2)
    assert result >= 1000


def test_view_reimbursement_statistics_three():
    result = reim_dao.view_reimbursement_statistics_three(2)
    assert result >= 2


def test_view_reimbursement_statistics_four():
    result = reim_dao.view_reimbursement_statistics_four(2)
    assert result > 100


def test_view_reimbursement_statistics_five():
    result = reim_dao.view_reimbursement_statistics_five(2)
    assert result < 200


def test_review_reimbursement_request():
    review = reim_dao.review_reimbursement_request(2)
    assert len(review) >= 2
