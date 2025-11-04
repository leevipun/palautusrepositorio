*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password confirmation  kalle123
    Click Button  Register
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  validpassword123
    Set Password confirmation  validpassword123
    Click Button  Register
    Username too short Should Be Shown

Register With Valid Username And Too Short Password
    Set Username  validuser
    Set Password  short
    Set Password confirmation  short
    Click Button  Register
    Password too short Should Be Shown

Register With Valid Username And Invalid Password
    Set Username  validuser
    Set Password  nopunctuation
    Set Password confirmation  nopunctuation
    Click Button  Register
    Password must contain at least one number or special character Should Be Shown

Register With Nonmatching Password And Password Confirmation
    Set Username  validuser
    Set Password  validpassword1
    Set Password confirmation  differentpassword1
    Click Button  Register
    Passwords do not match Should Be Shown

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  validpassword1
    Set Password confirmation  validpassword1
    Click Button  Register
    Go to Registration Page
    Set Username  kalle
    Set Password  anotherpassword1
    Set Password confirmation  anotherpassword1    
    Click Button  Register
    Username already taken Should Be Shown

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Username too short Should Be Shown
    Page Should Contain  Username must be at least 3 characters long

Password too short Should Be Shown
    Page Should Contain  Password must be at least 8 characters long

Password must contain at least one number or special character Should Be Shown
    Page Should Contain  Password must contain at least one number or special character

Passwords do not match Should Be Shown
    Page Should Contain  Passwords do not match

Username already taken Should Be Shown
    Page Should Contain  Username already taken

Go to Registration Page
    Go To  ${REGISTER_URL}