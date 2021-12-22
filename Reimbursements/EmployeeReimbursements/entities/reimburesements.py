class Reimbursements:
    def __init__(self, transaction_id: int, employee_id: int,
                 reimbursement_amount: int, expense_reason: str, status: str, manager_comment: str,
                 date: str):
        self.transaction_id = transaction_id
        self.employee_id = employee_id
        self.reimbursement_amount = reimbursement_amount
        self.expense_reason = expense_reason
        self.status = status
        self.manager_comment = manager_comment
        self.date = date

    def __str__(self):
        return "transactionId {}," "employeeId {}," \
               "reimbursementAmount {}," \
               "expenseReason {}," "status {}," \
               "managerComment {}""date {}," \
            .format(self.transaction_id, self.employee_id,
                    self.reimbursement_amount,
                    self.expense_reason, self.status,
                    self.date, self.manager_comment)

    def make_reimbursement_dictionary(self):
        return {
            "transactionId": self.transaction_id,
            "employeeId": self.employee_id,
            "reimbursementAmount": self.reimbursement_amount,
            "expenseReason": self.expense_reason,
            "status": self.status,
            "managerComment": self.manager_comment,
            "date": self.date
        }
