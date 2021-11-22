*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pekka  pekka123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  as  kalle123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  asd  asd123a
    Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  asd  qwertyui
    Output Should Contain  Invalid password

***Keywords***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123