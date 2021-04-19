import sys

import pandas as pd
from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


driver = webdriver.Firefox(
    executable_path=GeckoDriverManager().install())
driver.get("http://192.168.137.14/Default.aspx?K=%27Y%27")
ele_username = driver.find_element_by_id("txtuser").send_keys("vignesh")
ele_password = driver.find_element_by_id("txtpass").send_keys("v1990h")
driver.find_element_by_id("btnLogin").click()
driver.get("http://192.168.137.14/crm_report/sourceRptSummary_cc.aspx")
wait = WebDriverWait(driver, 10)


for i in range (1,19):

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
    from_date.send_keys(f'2021-04-{i}')
    to_date.send_keys(f'2021-04-{i}')
    sleep(2)
    search_btn.click()
    sleep(4)
    from_date = wait.until(
        EC.visibility_of_element_located(
            (By.ID, 'ContentPlaceHolder1_txtFromDate')))
    date_value = from_date.get_attribute('value')
    html_page = driver.page_source
    table = pd.read_html(html_page)
    table = table[8]
    table["Date"] = date_value
    sleep(2)
    table.to_csv('pandas_numpy\Files\crm.csv', mode='a',
                    header=False, index=False)


