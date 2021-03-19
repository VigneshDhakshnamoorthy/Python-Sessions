from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.delete_all_cookies()
driver.get("http://demo.guru99.com/test/drag_drop.html")
driver.implicitly_wait(10)
driver.maximize_window()

action = ActionChains(driver)
source = driver.find_element_by_id("credit2")
target = driver.find_element_by_id("bank")
action.drag_and_drop(source, target).perform()

sleep(2)

source = driver.find_element_by_id("fourth")
target = driver.find_element_by_id("amt7")
action.click_and_hold(source).move_to_element(target).release(target).perform()

sleep(2)

source = driver.find_element_by_id("credit1")
target = driver.find_element_by_id("loan")
action.drag_and_drop(source, target).perform()

sleep(2)

source = driver.find_element_by_id("fourth")
target = driver.find_element_by_id("amt8")
action.click_and_hold(source).move_to_element(target).release(target).perform()

sleep(2)

while True:
    try:
        match_or_not = driver.find_element_by_id("equal")
        print(match_or_not.text)
        break
    except NoSuchElementException:
        print("Drag and Drop Failed")
        break

driver.quit()
