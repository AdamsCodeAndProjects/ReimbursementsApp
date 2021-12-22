class Employee:
    def __init__(self, first_name: str, last_name: str, employee_id: int,
                 password: str, manager: bool):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.password = password
        self.manager = manager

    def __str__(self):
        return "first name {} " \
               "last name {}" \
               "employee Id {}" \
               "password {}" \
               "manager {} ".format(self.first_name, self.last_name,
                                    self.employee_id,
                                    self.password, self.manager)

    def make_employee_dictionary(self):
        return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "employeeId": self.employee_id,
            "password": self.password,
            "manager": self.manager
        }
