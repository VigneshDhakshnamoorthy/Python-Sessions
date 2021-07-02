*** Settings ***
Documentation     Selecting items from dropdown menus (Selenium).
Library           RPA.Browser.Selenium

*** Tasks ***
Select value from dropdown menu
    Open Available Browser  https://ccxuf.csb.app/
    Wait Until Element Is Visible   id:famous-robots
    Select From List By Value   id:famous-robots    wall-e
    Capture Page Screenshot
    [Teardown]  Close All Browsers
