import sys
sys.path.append(".")

from Page_Object_Model.login_page import LoginPage
from Page_Object_Model.browser_setup import driver, sleep, URL


driver.get(URL)

login = LoginPage(driver)
login.enter_details("standard_user", "secret_sauce")

print(driver.title)

sleep(2)
driver.quit()
