from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = None


def driver_open():
    global driver
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
