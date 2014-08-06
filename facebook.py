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
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='uiHeaderActions']/a[2]"))
    )
finally:
    driver.find_element_by_xpath("//div[@class='uiHeaderActions']/a[2]").click()

sleep(3)

number_friends = int(driver.find_element_by_xpath("//span[@class='_3d0']").text)
print("You have " + str(number_friends) + " friends on FB")

sleep(2)
driver.execute_script("window.scrollTo(0, 3500)")
sleep(3)
elem = driver.find_elements_by_class_name("_698")


driver.close()
