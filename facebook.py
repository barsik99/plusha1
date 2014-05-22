__author__ = 'Anastasiya'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")
elem = driver.find_element_by_id("email")
elem.send_keys("stasy_19@ngs.ru")
elem = driver.find_element_by_id("pass")
elem.send_keys("tel6502158425")
driver.find_element_by_id("loginbutton").click()
driver.find_element_by_link_text("FRIENDS").click()
#elem = driver.find_element_by_link_text("See All Friends").click()

try:
    wait = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located(By.XPATH, "//div[@class='uiHeaderActions']/a[2]")
    )
    driver.find_element_by_xpath().click()
