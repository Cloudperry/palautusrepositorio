*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Check Title
Test Teardown  Reset Application
# Vikat kaksi testiä olisivat olleet vähän lyhyempiä, jos ne käyttäisivät
# aikaisempien testien käyttäjätilejä, mutta päätin resetoida serverin testien välissä.

*** Test Cases ***
Register With Valid Username And Password
    Set Username  roni
    Set Password  roni1234
	Set Password Confirmation  roni1234
    Submit Registration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  r
    Set Password  roni1234
	Set Password Confirmation  roni1234
    Submit Registration
	Register Should Fail With Message  Username is too short or contains characters other than lowercase letters

Register With Valid Username And Too Short Password
    Set Username  roni
    Set Password  roni123
	Set Password Confirmation  roni123
    Submit Registration
	Register Should Fail With Message  Password is too short or contains only lowercase letters

Register With Nonmatching Password And Password Confirmation
    Set Username  roni
    Set Password  roni1234
	Set Password Confirmation  roni12345
    Submit Registration
	Register Should Fail With Message  Password confirmation doesn't match password

Login After Successful Registration
    Set Username  roni
    Set Password  roni1234
	Set Password Confirmation  roni1234
    Submit Registration
    Register Should Succeed
	Go To Login Page
	Set Username  roni
	Set Password  roni1234
	Submit Login
	Login Should Succeed

Login After Failed Registration
    Set Username  roni
    Set Password  roni1234
	Set Password Confirmation  roni12345
    Submit Registration
	Register Should Fail With Message  Password confirmation doesn't match password
	Go To Login Page
	Set Username  roni
	Set Password  roni1234
	Submit Login
	Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Go To Register Page And Check Title
	Go To Register Page
    Register Page Should Be Open
