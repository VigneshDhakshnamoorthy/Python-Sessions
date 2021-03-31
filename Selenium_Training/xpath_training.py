from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.delete_all_cookies()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://demo.guru99.com/test/selenium-xpath.html")

# Basic XPath:
ele = driver.find_element_by_xpath("//input[@name='uid']")
print(ele)

# Contains():
ele = driver.find_elements_by_xpath("//*[contains(@type,'sub')]")
print(ele)
ele = driver.find_elements_by_xpath("//*[contains(@id,'message')]")
print(ele)

# Using OR & AND :
ele = driver.find_elements_by_xpath("//*[@type='submit' or @name='btnReset']")
print(ele)
ele = driver.find_elements_by_xpath("//input[@type='submit' and @name='btnLogin']")
print(ele)

# Xpath Starts-with:
ele = driver.find_elements_by_xpath("//label[starts-with(@id,'message')]")
print(ele)

# XPath Text() Function :
ele = driver.find_element_by_xpath("//td[text()='UserID']")
print(ele.text)

# XPath axes methods:
# Following:
ele = driver.find_element_by_xpath("//*[@type='text']//following::input")
print(ele.text)
ele = driver.find_element_by_xpath("//*[@type='text']//following::input[1]")
print(ele.text)

# Ancestor:
ele = driver.find_element_by_xpath("//*[text()='Enterprise Testing']//ancestor::div")
print(ele.text)
ele = driver.find_element_by_xpath("//*[text()='Enterprise Testing']//ancestor::div[1]")
print(ele.text)

# Child:
ele = driver.find_element_by_xpath("//*[@id='java_technologies']//child::li")
print(ele.text)
ele = driver.find_element_by_xpath("//*[@id='java_technologies']//child::li[1]")
print(ele.text)

# Preceding:
ele = driver.find_element_by_xpath("//*[@type='submit']//preceding::input")
print(ele.text)
ele = driver.find_element_by_xpath("//*[@type='submit']//preceding::input[1]")
print(ele.text)

# Following-sibling:
ele = driver.find_element_by_xpath("//*[@type='submit']//following-sibling::input")
print(ele.text)

# Parent:
ele = driver.find_element_by_xpath("//*[@id='rt-feature']//parent::div")
print(ele.text)
ele = driver.find_element_by_xpath("//*[@id='rt-feature']//parent::div[1]")
print(ele.text)

# Self:
ele = driver.find_element_by_xpath("//*[@type='password']//self::input")
print(ele.text)

# Descendant:
ele = driver.find_element_by_xpath("//*[@id='rt-feature']//descendant::a")
print(ele.text)
ele = driver.find_element_by_xpath("//*[@id='rt-feature']//descendant::a[1]")
print(ele.text)


driver.quit()
