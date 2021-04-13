from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from webdriver_manager.firefox import GeckoDriverManager

url = "http://arkintech.com/"


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser.implicitly_wait(10)
    yield browser
    # For cleanup, quit the driver
    browser.quit()

  
def test_get_url(browser):
    browser.get(url)


def test_goto_contact_us(browser):
    browser.find_element_by_link_text("Contact Us").click()


def test_fill_forms(browser):
    browser.find_element_by_id("txtFName").send_keys("Vignesh")
    sleep(2)
