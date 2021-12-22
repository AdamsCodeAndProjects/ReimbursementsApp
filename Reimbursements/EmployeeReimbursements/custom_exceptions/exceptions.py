class IncorrectLoginCredentialsException(Exception):
    def __init__(self, message):
        self.message = message


class ReimburseNegativeAmountException(Exception):
    def __init__(self, message):
        self.message = message


class TooMuchMoneyException(Exception):
    def __init__(self, message):
        self.message = message


class NegativeTransactionIdException(Exception):
    def __init__(self, message):
        self.message = message


class DuplicateTransactionIdException(Exception):
    def __init__(self, message):
        self.message = message


class MustBeNumberValueException(Exception):
    def __init__(self, message):
        self.message = message
