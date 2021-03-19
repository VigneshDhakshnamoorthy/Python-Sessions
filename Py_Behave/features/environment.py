from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from behave import *


def before_all(context):
    context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    context.driver.delete_all_cookies()
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()


def after_all(context):
    context.driver.quit()


def before_feature(context, feature):
    print("before_feature activated --- " + context.feature.name)


def after_feature(context, feature):
    print("after_feature activated --- " + context.feature.name)


def before_scenario(context, scenario):
    if 'single' in context.tags:
        print("before_scenario activated -- " + context.scenario.name)


def after_scenario(context, scenario):
    if 'single' in context.tags:
        print("after_scenario activated -- " + context.scenario.name)


def before_tag(context, tag):
    print("before_tag activated")


def after_tag(context, tag):
    print("after_tag activated")


def before_step(context, step):
    print("before_step activated")


def after_step(context, step):
    print("after_step activated")
