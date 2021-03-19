from selenium import webdriver
from Page_Object_Model.login_page import LoginPage
from time import sleep
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.delete_all_cookies()
driver.implicitly_wait(10)

URL = "https://www.saucedemo.com/"
