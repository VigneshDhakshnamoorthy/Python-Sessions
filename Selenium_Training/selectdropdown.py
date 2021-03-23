from selenium import webdriver
from selenium.webdriver.support.ui import *

from webdriver_manager.firefox import GeckoDriverManager

option = webdriver.FirefoxOptions()

option.add_argument("-private")
option.add_argument("--window-size=1280,1024")


driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=option)
driver.implicitly_wait(30)

driver.get("http://demo.guru99.com/test/newtours/register.php")

country_menu = Select(driver.find_element_by_xpath("//*[@name='country']"))
country_name = country_menu.options

for name in country_name:
    print(name.text)

print(country_menu.is_multiple)
country_menu.select_by_visible_text("SERBIA")
print(country_menu.first_selected_option.text)
driver.quit()

