*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Confirm

***Test Cases***
Register With Valid Username And Password
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  as
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Submit Credentials
    Register Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  pekka
    Set Password  asdqwer
    Set Password Confirmation  asdqwer
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  pekka1234
    Submit Credentials
    Register Should Fail With Message  The passwords did not match

Login After Successful Registration
    Set Username  pallo
    Set Password  pallo1234
    Set Password Confirmation  pallo1234
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  pallo
    Set Password  pallo1234
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Set Username  kallo
    Set Password  kallo1234
    Set Password Confirmation  kkkallo1234
    Submit Credentials
    Register Should Fail With Message  The passwords did not match
    Go To Login Page
    Set Username  kallo
    Set Password  kallo1234
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

***Keywords***
Go To Register Page And Confirm
    Go To Register Page
    Register Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}