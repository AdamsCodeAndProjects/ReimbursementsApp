from typing import List

from flask import Flask, request, jsonify

from flask_cors import CORS
from custom_exceptions.exceptions import DuplicateTransactionIdException, NegativeTransactionIdException, \
    ReimburseNegativeAmountException, TooMuchMoneyException, MustBeNumberValueException, \
    IncorrectLoginCredentialsException
from data_access_layer.abstract_layer.employee_dao import EmployeeDAO
from data_access_layer.abstract_layer.reimbursements_dao import ReimbursementsDAO
from data_access_layer.implementation_classes.employee_imp import EmployeeDAOImp
from data_access_layer.implementation_classes.reimbursements_imp import ReimbursementsImp
from entities.employee import Employee
from entities.reimburesements import Reimbursements
from service_layer.abstract_service.employee_service import EmployeeService
from service_layer.abstract_service.reimbursement_service import ReimbursementService
from service_layer.implementation_services.employee_service_imp import EmployeeImpService
from service_layer.implementation_services.reimbursements_service_imp import ReimbursementServiceImp
import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app = Flask(__name__)
CORS(app)

employee_dao = EmployeeDAOImp()
employee_service = EmployeeImpService(employee_dao)
reimbursements_dao = ReimbursementsImp()
reimbursements_service = ReimbursementServiceImp(reimbursements_dao)


@app.post("/employee/login")
def employee_login_request():
    try:
        employee_data = request.get_json()
        login_credentials = employee_service.employee_login_request(employee_data["employeeId"],
                                                                    employee_data["password"])
        return jsonify(login_credentials), 200
    except IncorrectLoginCredentialsException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message), 400


@app.post("/reimbursements/create")
def create_reimbursement_request():
    try:
        body = request.get_json()
        new_reimbursement = Reimbursements(
            body["transactionId"],
            body["employeeId"],
            body["reimbursementAmount"],
            body["expenseReason"],
            body["status"],
            body["managerComment"],
            body["date"]
        )
        newly_created_request = reimbursements_service.service_create_reimbursement_request(new_reimbursement)
        created_request_as_dict = newly_created_request.make_reimbursement_dictionary()
        return jsonify(created_request_as_dict), 200
    except ReimburseNegativeAmountException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message), 400
    except TooMuchMoneyException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message), 400
    except MustBeNumberValueException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message), 400


@app.patch("/reimbursements/approval/<transaction_id>")
def reimbursement_request_approval(transaction_id: str):
    try:
        approve_data = request.get_json()
        new_update = approve_data["status"]
        returned_request = reimbursements_service.service_get_reimbursement_by_id(int(transaction_id))
        updated_account = reimbursements_service.service_reimbursement_request_approval(returned_request.transaction_id,
                                                                                        new_update)
        updated_reim_as_dictionary = updated_account.make_reimbursement_dictionary()
        return jsonify(updated_reim_as_dictionary), 200
    except NegativeTransactionIdException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message)


@app.patch("/reimbursements/comment/<transaction_id>")
def comment_about_reimbursement_request(transaction_id: str):
    try:
        approve_data = request.get_json()
        new_update = approve_data["managerComment"]
        returned_request = reimbursements_service.service_get_reimbursement_by_id(int(transaction_id))
        updated_account = reimbursements_service.service_comment_about_reimbursement_request(new_update,
                                                                                             returned_request.transaction_id)
        updated_reim_as_dictionary = updated_account.make_reimbursement_dictionary()
        return jsonify(updated_reim_as_dictionary), 200
    except NegativeTransactionIdException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message), 400


@app.get("/reimbursements/pending")
def view_pending_reimbursement_requests():
    pending_requests = reimbursements_service.service_view_pending_reimbursement_requests()
    reims_as_dictionaries = []
    for r in pending_requests:
        dictionary_reims = r.make_reimbursement_dictionary()
        reims_as_dictionaries.append(dictionary_reims)
    return jsonify(reims_as_dictionaries), 200


@app.get("/reimbursements/past")
def view_past_reimbursement_requests():
    rev = reimbursements_service.service_view_past_reimbursement_requests()
    reims_as_dictionaries = []
    for r in rev:
        dictionary_reims = r.make_reimbursement_dictionary()
        reims_as_dictionaries.append(dictionary_reims)
    return jsonify(reims_as_dictionaries), 200


# avg
@app.get("/reimbursements/stats/one/<employee_id>")
def view_reimbursement_statistics_one(employee_id: str):
    reimburse = reimbursements_service.service_view_reimbursement_statistics_one(int(employee_id))
    return jsonify(reimburse), 200


# sum
@app.get("/reimbursements/stats/two/<employee_id>")
def view_reimbursement_statistics_two(employee_id: int):
    reimburse = reimbursements_service.service_view_reimbursement_statistics_two(int(employee_id))
    return jsonify(reimburse), 200


# count
@app.get("/reimbursements/stats/three/<employee_id>")
def view_reimbursement_statistics_three(employee_id: int):
    reimburse = reimbursements_service.service_view_reimbursement_statistics_three(int(employee_id))
    return jsonify(reimburse), 200


# max
@app.get("/reimbursements/stats/four/<employee_id>")
def view_reimbursement_statistics_four(employee_id: int):
    reimburse = reimbursements_service.service_view_reimbursement_statistics_four(employee_id)
    return jsonify(reimburse), 200


# min
@app.get("/reimbursements/stats/five/<employee_id>")
def view_reimbursement_statistics_five(employee_id: int):
    reimburse = reimbursements_service.service_view_reimbursement_statistics_five(employee_id)
    return jsonify(reimburse), 200


@app.get("/reimbursements/review/<employee_id>")
def review_reimbursement_request(employee_id: int):
    review = reimbursements_service.service_review_reimbursement_request(employee_id)
    reviews_as_dictionary = []
    for rev in review:
        dictionary_rev = rev.make_reimbursement_dictionary()
        reviews_as_dictionary.append(dictionary_rev)
    return jsonify(reviews_as_dictionary), 200


app.run()
