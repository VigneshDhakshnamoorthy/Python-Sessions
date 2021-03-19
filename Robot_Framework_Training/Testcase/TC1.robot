*** Settings ***
Library  SeleniumLibrary
Library  gecksync.py

*** Variables ***
${LOGIN URL}      http://www.google.com
${BROWSER}        webdrivermanager firefox chrome --linkpath /usr/local/bin

*** Test Cases ***
LoginTest
    Open Browser To Login Page

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}