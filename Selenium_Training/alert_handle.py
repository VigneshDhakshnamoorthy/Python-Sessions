from time import sleep

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.delete_all_cookies()
driver.get("http://demo.automationtesting.in/Alerts.html")
driver.implicitly_wait(10)
driver.maximize_window()

Alert_List = driver.find_elements_by_xpath("//*[@class='tabpane pullleft']/ul/li")

Alert_List[0].click()
sleep(2)
driver.find_element_by_xpath("//*[@id='OKTab']/button").click()
alert_box = driver.switch_to.alert
print("-" * 15)
print("Simple Alert")
print(alert_box.text)
sleep(2)
alert_box.accept()
sleep(2)

Alert_List[1].click()
sleep(2)
driver.find_element_by_xpath("//*[@id='CancelTab']/button").click()
alert_box = driver.switch_to.alert
sleep(2)
alert_box.accept()
print("-" * 15)
print("Confirmation Alert")
print(driver.find_element_by_xpath("//*[@id='CancelTab']/p").text)
sleep(2)
driver.find_element_by_xpath("//*[@id='CancelTab']/button").click()
alert_box = driver.switch_to.alert
sleep(2)
alert_box.dismiss()
print(driver.find_element_by_xpath("//*[@id='CancelTab']/p").text)
print("-" * 15)
sleep(2)

Alert_List[2].click()
sleep(2)
driver.find_element_by_xpath("//*[@id='Textbox']/button").click()
alert_box = driver.switch_to.alert
sleep(2)
alert_box.send_keys("Vignesh")
alert_box.accept()
print("Prompt Alert")
print(driver.find_element_by_xpath("//*[@id='Textbox']/p").text)
print("-" * 15)

sleep(2)
driver.quit()
