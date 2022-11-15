import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org")
time.sleep(5)
driver.close()
