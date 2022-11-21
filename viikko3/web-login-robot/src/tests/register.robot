*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Check Title

*** Test Cases ***
Register With Valid Username And Password
    Set Username  roni
    Set Password  roni1234
	Set Password Confirmation  roni1234
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  r
    Set Password  roni1234
	Set Password Confirmation  roni1234
    Submit Credentials
	Register Should Fail With Message  Username is too short or contains characters other than lowercase letters

Register With Valid Username And Too Short Password
    Set Username  roni
    Set Password  roni123
	Set Password Confirmation  roni123
    Submit Credentials
	Register Should Fail With Message  Password is too short or contains only lowercase letters

Register With Nonmatching Password And Password Confirmation
    Set Username  roni
    Set Password  roni1234
	Set Password Confirmation  roni12345
    Submit Credentials
	Register Should Fail With Message  Password confirmation doesn't match password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Go To Register Page And Check Title
	Go To Register Page
    Register Page Should Be Open
