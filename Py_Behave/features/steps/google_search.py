from behave import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager


@given(u'open browser')
def open_browser(context):
    context.driver.get("https://www.google.com")


@when(u'search element with "{name}"')
def search_element(context, name):
    context.driver.find_element_by_name("q").send_keys(name, Keys.ENTER)


@then(u'back to homepage')
def back_homepage(context):
    sleep(3)
    context.driver.back()
    context.title = context.driver.title

    if context.title == "Google":
        assert True, "Title Correct"

    else:
        assert False, "Title Mismatch"
