from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.delete_all_cookies()
driver.get("http://arkintech.com/")
driver.implicitly_wait(10)
driver.maximize_window()
our_services = driver.find_element_by_link_text("Our Services")
our_services.click()

python_development = driver.find_element_by_link_text("Python Development")
python_development.send_keys(Keys.CONTROL + Keys.RETURN)
sleep(1)

big_data = driver.find_element_by_link_text("Big Data")
big_data.send_keys(Keys.CONTROL + Keys.RETURN)
sleep(2)

tabs = driver.window_handles
tabs_dic = {}

for tab in tabs:
    driver.switch_to.window(tab)
    tabs_dic[driver.current_url] = tab
    sleep(2)

driver.switch_to.window(tabs_dic["http://arkintech.com/"])

our_vision = WebDriverWait(driver, 2).until(
    EC.presence_of_element_located((By.ID, "three-accordion-item-1")))

our_vision.click()

sleep(1)

print("-" * 78)

stat_mes = str(driver.find_element_by_xpath("//*[@id=\"collapse-three-accordion-item-1\"]/div").text).split('. ')
for stat in stat_mes:
    print(stat)

print("-" * 78)

sleep(1)
print(tabs_dic)
sleep(2)
driver.quit()
