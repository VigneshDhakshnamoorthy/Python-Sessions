from time import sleep

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.delete_all_cookies()
driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.implicitly_wait(10)
driver.maximize_window()
sleep(1)
driver.switch_to.frame("frame-top")
sleep(1)
driver.switch_to.frame("frame-middle")
print(driver.find_element_by_id("content").text)
sleep(1)
driver.switch_to.default_content()
sleep(1)
driver.quit()

