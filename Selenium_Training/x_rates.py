from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
import time

time_in = time.perf_counter()

option = webdriver.FirefoxOptions()
option.add_argument('--headless')
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=option)
driver.delete_all_cookies()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.x-rates.com/table/?from=INR&amount=1")

wait = WebDriverWait(driver, 10)
element = wait.until(
    expected_conditions.visibility_of_element_located((By.ID, "yie-close-button-ef6e837e-b88f-51a0-afe1-a980e9790829")))

element.click()

element_country_names = driver.find_elements_by_xpath("//*[@class='tablesorter ratesTable']/tbody/tr/td[1]")
country_names = [element.text for element in element_country_names]
country_values = {}
for country in country_names:
    country_values[country] = float(driver.find_element_by_xpath(
        f"//table[@class='tablesorter ratesTable']/tbody/tr/td[text()='{country}']/ancestor::tr/td[3]").text)

for key, value in country_values.items():
    if value == max(country_values.values()):
        print(f'Highest Country Value : {key} || Value : {value} ')

time_out = time.perf_counter()
print(f'Taken {time_out - time_in}')
driver.quit()
