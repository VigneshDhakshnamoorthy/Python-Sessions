*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${LOGIN URL}      http://www.google.com
${BROWSER}        Firefox

*** Test Cases ***
LoginTest
    Open Browser    ${LOGIN URL}    ${BROWSER}
    close all browsers

*** Keywords ***
