__author__ = 'Anastasiya'

import os
from selenium import webdriver

chromedriver = "C:/Users/Anastasiya/Downloads/chromedriver_win32/chromedriver.exe"
print(chromedriver)
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://stackoverflow.com")
driver.quit()
