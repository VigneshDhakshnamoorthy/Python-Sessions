*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Test Cases ***
LoginTest
    open browser  https://www.google.com firefox
    input text  name:q


*** Keywords ***
