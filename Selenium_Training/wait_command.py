from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WaitCom:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_id(self, id_name):
        self.element = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, id_name)))
        print(id_name)
