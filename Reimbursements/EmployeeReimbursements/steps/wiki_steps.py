from behave import Given, When, Then
import time

#    ---------- Employee Login
from webdriver_manager import driver


@Given(u'The employee is on the login page')
def get_login_home(context):
    context.driver.get("http://127.0.0.1:5500/FolderForHTML/trial.html")


@When(u'The employee enters their employee id and password in the input boxes')
def enter_info_into_boxes(context):
    context.wiki_home.select_username_input().send_keys(5)
    context.wiki_home.select_password_input().send_keys("venom")


@When(u'The employee clicks the submit button')
def submit_login_button_clicked(context):
    context.wiki_home.select_login_button().click()


@Then(u'The employee should be logged in and redirected to the employee home page')
def employee_to_employee_page(context):
    time.sleep(2)
    title = context.driver.title
    assert title == "Daily Bugle Logged In"


# #    -------------------- Employee Submit new Request

@Given(u'The employee is still on the employee page')
def get_employee_login_home_for_new_req(context):
    context.driver.get("http://127.0.0.1:5500/FolderForHTML/page2.html")


@When(u'The employee enters amounts in the employee id, request amount, reason, and date boxes')
def enter_info_into_reimbursement_boxes(context):
    context.wiki_home.select_employ_id_request().send_keys(5)
    context.wiki_home.select_amount_for_reim().send_keys(15)
    context.wiki_home.select_reason_for_reim().send_keys("test")
    context.wiki_home.select_date_for_reim().send_keys("2021/12/22")


@When(u'The employ clicks the submit request button')
def click_submit_new_request_button(context):
    context.wiki_home.select_submit_request_button().click()


@Then(u'The employee should get an alert saying request submitted')
def request_complete(context):
    time.sleep(2)
    assert context.driver.switch_to.alert.text == "Request submitted"
    context.driver.switch_to.alert.accept()


# #  ----------------      review my reimbursement requests


@Given(u'The employee is on the employee page')
def get_login_home_for_emp(context):
    context.driver.get("http://127.0.0.1:5500/FolderForHTML/page2.html")


@When(u'When the employee clicks the table')
def click_table(context):
    context.wiki_home.select_tables().click()


@Then(u'The employee should see his past requests')
def see_past_requests(context):
    title = context.driver.title
    assert title == "Daily Bugle Logged In"

    #  ------------------------- System Negative Values ----------------------


@Given(u'The user is on the employee page logged in')
def user_attempt_to_use_negatives(context):
    context.driver.get("http://127.0.0.1:5500/FolderForHTML/page2.html")


@When(u'The user enters a negative value into the amount')
def user_attempt_to_type_negative_amount(context):
    context.wiki_home.select_employ_id_request().send_keys(4)
    context.wiki_home.select_amount_for_reim().send_keys(-15)
    context.wiki_home.select_reason_for_reim().send_keys("test")
    context.wiki_home.select_date_for_reim().send_keys("2021/12/22")


@When(u'The user clicks submit for negative values')
def click_submit_new_request_button(context):
    context.wiki_home.select_submit_request_button().click()


@Then(u'An alert pops up stating cannot use negatives')
def system_alert_pops_up(context):
    time.sleep(2)
    assert context.driver.switch_to.alert.text == "Cannot request negative amounts!"
    context.driver.switch_to.alert.accept()

    #  ----------------  Employee Logout


@Given(u'The employee is logged in the employee page')
def get_login_home_for_employee(context):
    context.driver.get("http://127.0.0.1:5500/FolderForHTML/page2.html")


@When(u'The employee clicks on the logout button')
def submit_logout_button_clicked(context):
    context.wiki_home.select_logout_button().click()


@Then(u'The employee is redirected back to the home page')
def employee_to_employee_page(context):
    time.sleep(.5)
    title = context.driver.title
    assert title == "Daily Bugle Reimbursements Page"


#     #  ---------------- Manager Login


@Given(u'The manager is on the login page')
def get_login_home_for_manager(context):
    context.driver.get("http://127.0.0.1:5500/FolderForHTML/trial.html")


@When(u'The manager enters their employee id and password in the input boxes')
def enter_info_into_boxes(context):
    context.wiki_home.select_username_input().send_keys("1")
    context.wiki_home.select_password_input().send_keys("banana")


@When(u'The manager clicks the submit button login')
def submit_login_button_clicked(context):
    context.wiki_home.select_login_button().click()


@Then(u'The manager should be logged in and redirected to the manager home page')
def manager_to_manager_page(context):
    time.sleep(2)
    title = context.driver.title
    assert title == "Manager Reimbursement Page"


# #  ----------------------  View Statistics 1 ----------------------
@Given(u'The manager is on the manager page for stat')
def get_manager_stat_one(context):
    context.driver.get("http://127.0.0.1:5500/FolderForHTML/page3.html")


@When(u'The manager enters the employee id in the stat one inputs')
def enter_trans_id_input(context):
    context.wiki_home.select_emp_id_stat_one_input().send_keys("4")


@When(u'The manager clicks on the submit button one')
def submit_login_button_clicked(context):
    context.wiki_home.select_statistics_button_one().click()


@Then(u'The manager can view a statistic one')
def element_changed(context):
    title = context.driver.title
    assert title == "Manager Reimbursement Page"


# #  ----------------------  View Statistics 2 ----------------------
@Given(u'The manager is on the manager page two')
def get_manager_home(context):
    context.driver.get("http://127.0.0.1:5500/FolderForHTML/page3.html")


@When(u'The manager enters the employee id in the statistics inputs two')
def enter_trans_id_input(context):
    context.wiki_home.select_emp_id_stat_two_input().send_keys("4")


@When(u'The manager clicks the submit button two')
def submit_login_button_clicked(context):
    context.wiki_home.select_statistics_button_two().click()


@Then(u'The manager can view a statistic two')
def element_changed(context):
    title = context.driver.title
    assert title == "Manager Reimbursement Page"


#
# #  ----------------------  View Statistics 3 ----------------------
@Given(u'The manager is on the manager page three')
def get_manager_home(context):
    context.driver.get("http://127.0.0.1:5500/FolderForHTML/page3.html")


@When(u'The manager enters the employee id in the statistics inputs three')
def enter_trans_id_input(context):
    context.wiki_home.select_emp_id_stat_three_input().send_keys("4")


@When(u'The manager clicks the submit button three')
def submit_login_button_clicked(context):
    context.wiki_home.select_statistics_button_three().click()


@Then(u'The manager can view a statistic three')
def element_changed(context):
    title = context.driver.title
    assert title == "Manager Reimbursement Page"


# #  ----------------------  View Statistics 4 ----------------------
@Given(u'The manager is on the manager page four')
def get_manager_home(context):
    context.driver.get("http://127.0.0.1:5500/FolderForHTML/page3.html")


@When(u'The manager enters the employee id in the statistics inputs four')
def enter_trans_id_input(context):
    context.wiki_home.select_emp_id_stat_four_input().send_keys("4")


@When(u'The manager clicks the submit button four')
def submit_login_button_clicked(context):
    context.wiki_home.select_statistics_button_four().click()


@Then(u'The manager can view a statistic four')
def element_changed(context):
    title = context.driver.title
    assert title == "Manager Reimbursement Page"


# #  ----------------------  View Statistics 5 ----------------------
@Given(u'The manager is on the manager page five')
def get_manager_home(context):
    context.driver.get("http://127.0.0.1:5500/FolderForHTML/page3.html")


@When(u'The manager enters the employee id in the statistics inputs five')
def enter_trans_id_input(context):
    context.wiki_home.select_emp_id_stat_five_input().send_keys("4")


@When(u'The manager clicks the submit button five')
def submit_login_button_clicked(context):
    context.wiki_home.select_statistics_button_five().click()


@Then(u'The manager can view a statistic five')
def element_changed(context):
    title = context.driver.title
    assert title == "Manager Reimbursement Page"


# #     -------------------------Leave Comment----------------

@Given(u'The manager is on the manager page comments')
def get_login_home(context):
    context.driver.get("http://127.0.0.1:5500/FolderForHTML/page3.html")


@When(u'The manager enters the transaction id into the input box comments')
def enter_trans_id_input(context):
    context.wiki_home.enter_trans_id_input().send_keys("5")


@When(u'The manager enters the comment into the comment box comments')
def enter_trans_id_input(context):
    context.wiki_home.select_enter_comment_into_input().send_keys("I think not")


@Then(u'The manager clicks submit comments')
def submit_login_button_clicked(context):
    context.wiki_home.submit_login_button_clicked().click()


# @Then(u'The request has been saved in the database comment')
# def element_changed(context):
#     context.wiki_home.change_of_element()


# #  -------------------  Approve / Deny Reimbursements -----------------

@Given(u'The manager is on the manager page comment')
def get_login_home(context):
    context.driver.get("http://127.0.0.1:5500/FolderForHTML/page3.html")


@When(u'The manager enters the transaction id into the input box')
def enter_transact_id_input(context):
    context.wiki_home.enter_transact_id_input().send_keys("34")


@When(u'The manager enters approve or deny into the input box')
def enter_approval_info_input(context):
    context.wiki_home.select_approval_info().send_keys("Denied")


@Then(u'The manager clicks the submit button')
def submit_button_clicked_for_approval(context):
    context.wiki_home.select_approval_button().click()


# @Then(u'The request has been updated and saved in the database comment')
# def element_changed(context):
#     context.wiki_home.change_of_element()


# # ------------------ View all pending requests --------------------
@Given(u'The manager is on the manager page pending')
def get_login_home(context):
    context.driver.get("http://127.0.0.1:5500/FolderForHTML/page3.html")


@Then(u'The manager should be able to see all pending requests pending')
def element_changed(context):
    title = context.driver.title
    assert title == "Manager Reimbursement Page"


# # ------------------ View all past requests --------------------
@Given(u'The manager is on the manager page requests')
def get_login_home(context):
    context.driver.get("http://127.0.0.1:5500/FolderForHTML/page3.html")


@Then(u'The manager should able to view any past reimbursement request requests')
def element_changed(context):
    title = context.driver.title
    assert title == "Manager Reimbursement Page"


# # ----------------- Manager Logout  --------------------------

@Given(u'The manager is logged in the manager page logout')
def get_login_home(context):
    context.driver.get("http://127.0.0.1:5500/FolderForHTML/page3.html")


@When(u'The manager clicks on the logout button')
def submit_login_button_clicked(context):
    context.wiki_home.select_logout_button().click()


@Then(u'The manager is redirected back to the home page')
def employee_to_home_page(context):
    time.sleep(.5)
    title = context.driver.title
    assert title == "Daily Bugle Reimbursements Page"


#  ---------------------------- System Login ----------------------
@Given(u'The user is on the login page')
def system_incorrect_login(context):
    context.driver.get("http://127.0.0.1:5500/FolderForHTML/trial.html")


@When(u'The user enters in incorrect credentials')
def system_bad_credentials(context):
    context.wiki_home.select_username_input().send_keys(22)
    context.wiki_home.select_password_input().send_keys("vvvvvvvvvvvv")


@When(u'The user clicks on the submit button of bad login info')
def system_hit_submit(context):
    context.wiki_home.select_login_button().click()


@Then(u'An alert pops up saying Bad Credentials')
def system_alert(context):
    time.sleep(2)
    assert context.driver.switch_to.alert.text == "Bad Login Credentials.  You're as bad as Spiderman!  Try Again."
    context.driver.switch_to.alert.accept()

