*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${LOGIN URL}      http://www.google.com
${chromedriver_path}  gecksync.gecko_sync
${BROWSER}        Firefox

*** Test Cases ***
LoginTest
    Open Browser    ${LOGIN URL}    ${BROWSER}
    close all browsers

*** Keywords ***
