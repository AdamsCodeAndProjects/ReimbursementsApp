from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager


class WikiHomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_username_input(self):
        element: WebElement = self.driver.find_element(By.ID, "username")
        return element

    def select_password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "password")
        return element

    def select_login_button(self):
        element: WebElement = self.driver.find_element(By.ID, "logbutton")
        return element

    #  --------------  Emp manage reimbursements ---------------------

    def select_employ_id_request(self):
        element: WebElement = self.driver.find_element(By.ID, "employee")
        return element

    def select_tables(self):
        element: WebElement = self.driver.find_element(By.ID, "reimbursementsTable")
        return element

    def select_amount_for_reim(self):
        element: WebElement = self.driver.find_element(By.ID, "amount")
        return element

    def select_reason_for_reim(self):
        element: WebElement = self.driver.find_element(By.ID, "reason")
        return element

    def select_date_for_reim(self):
        element: WebElement = self.driver.find_element(By.ID, "date")
        return element

    def select_new_request_button_for_approval(self):
        element: WebElement = self.driver.find_element(By.ID, "createrequestbutton")
        return element

    # ----------------------  Logout  ---------------------------

    def select_logout_button(self):
        element: WebElement = self.driver.find_element(By.ID, "logoutbutton")
        return element

    def select_info_for_request(self):
        element: WebElement = self.driver.find_element(By.ID, "employee")
        return element

    def select_info_for_request_amount(self):
        element: WebElement = self.driver.find_element(By.ID, "amount")
        return element

    def select_info_for_request_reason(self):
        element: WebElement = self.driver.find_element(By.ID, "reason")
        return element

    def select_info_for_request_date(self):
        element: WebElement = self.driver.find_element(By.ID, "date")
        return element

    def select_submit_request_button(self):
        element: WebElement = self.driver.find_element(By.ID, "createrequestbutton")
        return element

    # -----------------  Stats ----------------------------

    def select_emp_id_stat_one_input(self):
        element: WebElement = self.driver.find_element(By.ID, "employeeIdForStatOne")
        return element

    def select_statistics_button_one(self):
        element: WebElement = self.driver.find_element(By.ID, "getStatsButton")
        return element

    def select_emp_id_stat_two_input(self):
        element: WebElement = self.driver.find_element(By.ID, "employeeIdForStatTwo")
        return element

    def select_statistics_button_two(self):
        element: WebElement = self.driver.find_element(By.ID, "getStatsButtonTwo")
        return element

    def select_emp_id_stat_three_input(self):
        element: WebElement = self.driver.find_element(By.ID, "employeeIdForStatThree")
        return element

    def select_statistics_button_three(self):
        element: WebElement = self.driver.find_element(By.ID, "getStatsButtonThree")
        return element

    def select_emp_id_stat_four_input(self):
        element: WebElement = self.driver.find_element(By.ID, "employeeIdForStatFour")
        return element

    def select_statistics_button_four(self):
        element: WebElement = self.driver.find_element(By.ID, "getStatsButtonFour")
        return element

    def select_emp_id_stat_five_input(self):
        element: WebElement = self.driver.find_element(By.ID, "employeeIdForStatFive")
        return element

    def select_statistics_button_five(self):
        element: WebElement = self.driver.find_element(By.ID, "getStatsButtonFive")
        return element

    # -------------------  Approve / Deny ------------------------------

    def enter_transact_id_input(self):
        element: WebElement = self.driver.find_element(By.ID, "transactIdBox")
        return element

    def select_approval_info(self):
        element: WebElement = self.driver.find_element(By.ID, "approvalBox")
        return element

    def select_approval_button(self):
        element: WebElement = self.driver.find_element(By.ID, "approvalSubmit")
        return element

    # -----------------  Manager Comment  ------------------------------

    def enter_trans_id_input(self):
        element: WebElement = self.driver.find_element(By.ID, "transIdBox")
        return element

    def select_enter_comment_into_input(self):
        element: WebElement = self.driver.find_element(By.ID, "commentBox")
        return element

    def submit_login_button_clicked(self):
        element: WebElement = self.driver.find_element(By.ID, "commentSubmit")
        return element

    def element_changed(self):
        element: WebElement = self.driver.find_element(By.ID, "reimbursementsBody")
        return element
