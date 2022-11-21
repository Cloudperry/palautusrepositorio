*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
	Input Credentials  roni  roni1234
	Output Should Contain  New user registered
	Run Application

Register With Already Taken Username And Valid Password
	Create User  roni  roni12344321
	Input Credentials  roni  roni1234
	Output Should Contain  User with username roni already exists
	Run Application

Register With Too Short Username And Valid Password
	Input Credentials  r  roni1234
	Output Should Contain  Username is too short or contains characters other than lowercase letters
	Run Application

Register With Valid Username And Too Short Password
	Input Credentials  roni  r123456
	Output Should Contain  Password is too short or contains only lowercase letters
	Run Application

Register With Valid Username And Long Enough Password Containing Only Letters
	Input Credentials  roni  RoninTestisalasana
	Output Should Contain  Password is too short or contains only lowercase letters
	Run Application

