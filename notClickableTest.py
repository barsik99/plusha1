__author__ = 'Anastasiya'

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By
import os
from selenium import webdriver

chromedriver = "C:/Users/Anastasiya/Downloads/chromedriver_win32/chromedriver.exe"
print(chromedriver)
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://www.google.com")

driver.find_element_by_name("q").send_keys("Eiffel tower");
sleep(1000);
driver.find_element_by_name("btnG").click();
driver.quit()
