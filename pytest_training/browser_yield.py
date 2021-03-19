import pytest
from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager

url = "http://arkintech.com/"


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser.implicitly_wait(10)
    yield browser
    # For cleanup, quit the driver
    browser.quit()


def test_get_title(browser):
    browser.get(url)


def test_goto_contact_us(browser):
    browser.find_element_by_link_text("Contact Us").click()
