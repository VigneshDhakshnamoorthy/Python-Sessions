import os

import pandas as pd
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

# option = webdriver.FirefoxOptions()
# option.add_argument('--headless')
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=option)
# driver.get("https://money.rediff.com/gainers/bse/daily/groupz")
# WebElement = driver.find_elements_by_xpath("//*[@class='dataTable']/tbody/tr/td[1]")

# companies = {"Company": [], "Group": [], "Prev Close (Rs)": [], "Current Price (Rs)": [], "% Change": []}

# for company in WebElement:
#     companies["Company"].append(
#         driver.find_element_by_xpath("//*[contains(text(),'" + company.text + "')]/ancestor::tr/td[1]").text)

#     companies["Group"].append(
#         driver.find_element_by_xpath("//*[contains(text(),'" + company.text + "')]/ancestor::tr/td[2]").text)

#     companies["Prev Close (Rs)"].append(float(str(
#         driver.find_element_by_xpath("//*[contains(text(),'" + company.text + "')]/ancestor::tr/td[3]").text).
#                                               replace(",", "")))

#     companies["Current Price (Rs)"].append(float(str(
#         driver.find_element_by_xpath("//*[contains(text(),'" + company.text + "')]/ancestor::tr/td[4]").text).
#                                                  replace(",", "")))

#     companies["% Change"].append(float(str(
#         driver.find_element_by_xpath("//*[contains(text(),'" + company.text + "')]/ancestor::tr/td[5]").text).
#                                        replace(" ", "")))

File_Loc = "Selenium_Training/Files/moneydata.xlsx"

# data_out = pd.DataFrame(companies)
# data_out.to_excel(File_Loc, index=False)
data_in = pd.read_excel(File_Loc, usecols=[0,1, 2, 3, 4, 5])
print(data_in)
# driver.quit()
