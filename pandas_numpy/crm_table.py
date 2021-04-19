import datetime
import sys

import pandas as pd
from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

option = webdriver.FirefoxOptions()
option.add_argument("--headless")
driver = webdriver.Firefox(
    executable_path=GeckoDriverManager().install(), options=option)
wait = WebDriverWait(driver, 15)
driver.implicitly_wait(15)
driver.get("http://192.168.137.14/Default.aspx?K=%27Y%27")
ele_username = driver.find_element_by_id("txtuser").send_keys("vignesh")
ele_password = driver.find_element_by_id("txtpass").send_keys("v1990h")
driver.find_element_by_id("btnLogin").click()
driver.get("http://192.168.137.14/crm_report/sourceRptSummary_cc.aspx")

start_date = datetime.date(year=2021, month=3, day=19)
end_date = datetime.date(year=2021, month=4,  day=18)

current_date = start_date
while current_date <= end_date:

    from_date = wait.until(
    EC.visibility_of_element_located(
        (By.ID, 'ContentPlaceHolder1_txtFromDate')))

    to_date = wait.until(
        EC.visibility_of_element_located(
            (By.ID, 'ContentPlaceHolder1_txtToDate')))

    search_btn = wait.until(
        EC.visibility_of_element_located(
            (By.ID, 'ContentPlaceHolder1_btnSearch')))


    from_date.clear()
    to_date.clear()
    from_date.send_keys(str(current_date))
    to_date.send_keys(str(current_date))
    search_btn.click()
    
    driver.implicitly_wait(15)
    
    from_date = wait.until(
        EC.visibility_of_element_located(
            (By.ID, 'ContentPlaceHolder1_txtFromDate')))
    date_value = from_date.get_attribute('value')
    html_page = driver.page_source
    table = pd.read_html(html_page)
    table = table[8]
    
    table["Date"] = date_value
    
    table.to_csv('pandas_numpy\Files\crm.csv', mode='a',
                    header=False, index=False)
    
    current_date += datetime.timedelta(days=1)



driver.quit()
