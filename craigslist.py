__author__ = 'Anastasiya'

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://sfbay.craigslist.org/")
search_form = driver.find_element_by_xpath("//form[@id='search']")
search_form.find_element_by_xpath("//input[@id='query']").send_keys("buick encore")
search_form.find_element_by_xpath("//select[@id='catAbb']/option[@value='sss']").click()
search_form.find_element_by_xpath("//input[@id='go']").click()

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "searchform"))
    )
finally:
    print("searchform")

searchform = driver.find_element_by_xpath("//form[@id='searchform']")
#searchform.find_element_by_xpath("//input[@id='it']").click()
#searchform.find_element_by_xpath("//input[@id='searchbtn']").click()

driver.get_screenshot_as_file("screenshot.png")



sleep(1)

toc_legend = driver.find_element_by_xpath("//div[@class='toc_legend']")
toc_legend.find_element_by_xpath("//span/a[@id='mapview']").click()

#driver.close()
