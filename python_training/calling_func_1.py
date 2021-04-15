from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager



def driver_open():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return driver