from abc import ABC
from typing import List

from data_access_layer.abstract_layer.reimbursements_dao import ReimbursementsDAO
from entities.reimburesements import Reimbursements
from util.database_connection import connection


class ReimbursementsImp(ReimbursementsDAO):

    def create_reimbursement_request(self, reimburse: Reimbursements) -> Reimbursements:
        sql = """INSERT INTO reimbursements VALUES(default, %s, %s, %s, %s, %s, %s)
                                returning transaction_id"""
        cursor = connection.cursor()
        cursor.execute(sql, (reimburse.employee_id, reimburse.reimbursement_amount,
                             reimburse.expense_reason, reimburse.status, reimburse.manager_comment,
                             reimburse.date))
        connection.commit()
        reim = cursor.fetchone()[0]
        reimburse.employee_id = reim
        return reimburse

    def reimbursement_request_approval(self, approval: str, transaction_id: int) -> Reimbursements:
        sql = "update reimbursements set status = %s where transaction_id = %s returning *"
        cursor = connection.cursor()
        cursor.execute(sql, (approval, transaction_id))
        connection.commit()
        account_record = cursor.fetchone()
        account = Reimbursements(*account_record)
        return account

    def comment_about_reimbursement_request(self, manager_comment: str, transaction_id: int) -> Reimbursements:
        sql = "update reimbursements set manager_comment = %s where transaction_id = %s returning *"
        cursor = connection.cursor()
        cursor.execute(sql, (manager_comment, transaction_id))
        connection.commit()
        account_record = cursor.fetchone()
        account = Reimbursements(*account_record)
        return account

    def view_pending_reimbursement_requests(self) -> List[Reimbursements]:
        sql = "select * from reimbursements where status = 'pending'"
        cursor = connection.cursor()
        cursor.execute(sql)
        account_records = cursor.fetchall()
        account_list = []
        for account in account_records:
            account_list.append(Reimbursements(*account))
        return account_list

    def view_past_reimbursement_requests(self) -> List[Reimbursements]:
        sql = "select * from reimbursements where status <> 'pending'"
        cursor = connection.cursor()
        cursor.execute(sql)
        account_records = cursor.fetchall()
        account_list = []
        for account in account_records:
            account_list.append(Reimbursements(*account))
        return account_list

    def view_reimbursement_statistics_one(self, employee_id: int):
        sql = "select avg(reimbursement_amount) from reimbursements where employee_id = %s;"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        reimburse_avg = cursor.fetchone()[0]
        return reimburse_avg

    def view_reimbursement_statistics_two(self, employee_id: int):
        sql = "select sum(reimbursement_amount) from reimbursements where employee_id = %s;"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        reimburse_sum = cursor.fetchone()[0]
        return reimburse_sum

    def view_reimbursement_statistics_three(self, employee_id: int):
        sql = "select count(reimbursement_amount) from reimbursements where employee_id = %s;"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        reimburse_sum = cursor.fetchone()[0]
        return reimburse_sum

    def view_reimbursement_statistics_four(self, employee_id: int):
        sql = "select max(reimbursement_amount) from reimbursements where employee_id = %s;"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        reimburse_sum = cursor.fetchone()[0]
        return reimburse_sum

    def view_reimbursement_statistics_five(self, employee_id: int):
        sql = "select min(reimbursement_amount) from reimbursements where employee_id = %s;"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        reimburse_sum = cursor.fetchone()[0]
        return reimburse_sum

    def review_reimbursement_request(self, employee_id: int) -> List[Reimbursements]:
        sql = "select * from reimbursements where employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        reim_records = cursor.fetchall()
        reim_list = []
        for reim in reim_records:
            reim_list.append(Reimbursements(*reim))
        return reim_list

    def get_reimbursement_by_id(self, transaction_id: int) -> Reimbursements:
        sql = "select * from reimbursements where transaction_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [transaction_id])
        re_record = cursor.fetchone()
        reimburse = Reimbursements(*re_record)
        return reimburse


