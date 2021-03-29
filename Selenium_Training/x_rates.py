from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait

option = webdriver.FirefoxOptions()
# option.add_argument('--headless')
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=option)
driver.delete_all_cookies()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.x-rates.com/table/?from=INR&amount=1")

driver = driver
wait = WebDriverWait(driver, 10)
element = wait.until(expected_conditions.visibility_of_element_located((By.ID, "yie-close-button-ef6e837e-b88f-51a0-afe1-a980e9790829")))

element.click()