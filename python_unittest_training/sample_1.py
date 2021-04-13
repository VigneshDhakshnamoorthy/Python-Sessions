import unittest
import os

import HtmlTestRunner
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.google.com")
        print(driver.title)
        print(os.getcwd())

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=os.getcwd()+'/python_unittest_training/HTMLTestRunner'))
