from behave import *


@when(u'we visit "{url}"')
def step_impl(context, url):
    context.browser.get(url)
    print(context.browser.title)


@then(u'it should have a title "{title}"')
def step_impl(context, title):
    if context.browser.title == title:
        assert True
    else:
        context.browser.get(" https://www.google.com")
        assert False
