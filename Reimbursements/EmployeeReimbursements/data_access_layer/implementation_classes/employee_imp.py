from psycopg2._psycopg import cursor

from data_access_layer.abstract_layer.employee_dao import EmployeeDAO
from entities.employee import Employee
from util.database_connection import connection


class EmployeeDAOImp(EmployeeDAO):
    def employee_login_request(self, employee_id: int, pass_word: str) -> bool:
        sql = "select last_name from employee where employee_id = %s and pass_word = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (employee_id, pass_word))
        validated = cursor.fetchone()
        return validated
