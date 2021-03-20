*** Settings ***
Library  SeleniumLibrary
Library  gecksync

*** Variables ***
${LOGIN URL}      http://www.google.com
${BROWSER}        gecksync.browser

*** Test Cases ***
LoginTest
    Open Browser To Login Page

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}