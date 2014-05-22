__author__ = 'Anastasiya'
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.odnoklassniki.ru/")
elem = driver.find_element_by_id("field_email")
elem.send_keys("stasy_19@ngs.ru")
elem = driver.find_element_by_id("field_password")
elem.send_keys("tel6502158425")
elem = driver.find_element_by_xpath('//input[@name="st.email"]')
#elem.send_keys("found")
#elem = driver.find_element_by_xpath('//input[@value="Log.in"]')
#elem = driver.f
#elem = driver.find_element_by_class("button-pro.button-pro_big.anonym_login_btn.inlineBlock")
elem = driver.find_element_by_link_text("Друзья")
