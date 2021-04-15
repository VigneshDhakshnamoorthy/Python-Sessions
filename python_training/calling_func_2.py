import sys
sys.path.append(".")

from python_training.calling_func_1 import driver_open

driver = driver_open()

def driver_open2():
    url_link = "http://demo.guru99.com/test/newtours/register.php"
    driver.get(url_link)


driver_open2()
