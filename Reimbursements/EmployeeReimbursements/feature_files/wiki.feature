Feature: Employee Login


  Scenario: As the employee I want to login to manage my reimbursements
    Given  The employee is on the login page
    When The employee enters their employee id and password in the input boxes
    When The employee clicks the submit button
    Then  The employee should be logged in and redirected to the employee home page

  Scenario: As the employee I should be able to submit new reimbursement request
    Given The employee is still on the employee page
    When The employee enters amounts in the employee id, request amount, reason, and date boxes
    When The employ clicks the submit request button
    Then The employee should get an alert saying request submitted

    Scenario: As the employee I should be able to review my reimbursement requests
      Given The employee is on the employee page
      When When the employee clicks the table
      Then The employee should see his past requests

  Scenario: As the employee I should be able to log out
    Given The employee is logged in the employee page
    When The employee clicks on the logout button
    Then The employee is redirected back to the home page

  Scenario: As the manager I want to login to manage my reimbursement decisions
    Given  The manager is on the login page
    When The manager enters their employee id and password in the input boxes
    When The manager clicks the submit button login
    Then  The manager should be logged in and redirected to the manager home page

  Scenario:  As a manager, I want to view multiple statistics 1
    Given The manager is on the manager page for stat
    When The manager enters the employee id in the stat one inputs
    When The manager clicks on the submit button one
    Then The manager can view a statistic one

  Scenario:  As a manager, I want to view multiple statistics 2
    Given The manager is on the manager page two
    When The manager enters the employee id in the statistics inputs two
    When The manager clicks the submit button two
    Then The manager can view a statistic two

     Scenario:  As a manager, I want to view multiple statistics 3
    Given The manager is on the manager page three
    When The manager enters the employee id in the statistics inputs three
    When The manager clicks the submit button three
    Then The manager can view a statistic three

  Scenario:  As a manager, I want to view multiple statistics 4
    Given The manager is on the manager page four
    When The manager enters the employee id in the statistics inputs four
    When The manager clicks the submit button four
    Then The manager can view a statistic four


  Scenario:  As a manager, I want to view multiple statistics 5
    Given The manager is on the manager page five
    When The manager enters the employee id in the statistics inputs five
    When The manager clicks the submit button five
    Then The manager can view a statistic five

  Scenario:  As a manager, I should be able to approve reimbursement requests
    Given The manager is on the manager page comment
    When The manager enters the transaction id into the input box
    When The manager enters approve or deny into the input box
    Then The manager clicks the submit button

  Scenario:  As a manager, I should be able to leave a comment on requests
    Given The manager is on the manager page comments
    When The manager enters the transaction id into the input box comments
    When The manager enters the comment into the comment box comments
    Then The manager clicks submit comments

  Scenario:  As a manager, I should be able to view all pending reimbursements
    Given The manager is on the manager page pending
    Then The manager should be able to see all pending requests pending

  Scenario:  As a manager, I should be able to view all past reimbursements
    Given The manager is on the manager page requests
    Then The manager should able to view any past reimbursement request requests

  Scenario: As the manager I should be able to log out
    Given The manager is logged in the manager page logout
    When The manager clicks on the logout button
    Then The manager is redirected back to the home page

  Scenario: As a system I should reject all failed login attempts
    Given The user is on the login page
    When The user enters in incorrect credentials
    When The user clicks on the submit button of bad login info
    Then An alert pops up saying Bad Credentials

  Scenario: As a system I should reject negative reimbursement values
    Given The user is on the employee page logged in
    When The user enters a negative value into the amount
    When The user clicks submit for negative values
    Then An alert pops up stating cannot use negatives
