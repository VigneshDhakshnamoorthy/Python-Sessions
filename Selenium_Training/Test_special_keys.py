from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.delete_all_cookies()
driver.get("https://www.geeksforgeeks.org/")
driver.implicitly_wait(10)
driver.maximize_window()

Topic_wise_Practice = driver.find_element_by_link_text("Topic-wise Practice")
action = ActionChains(driver)

action.context_click(Topic_wise_Practice).key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).send_keys(
    Keys.ENTER).key_up(Keys.CONTROL).perform()
sleep(4)
driver.quit()



