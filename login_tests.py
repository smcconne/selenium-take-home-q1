from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
# Local imports
import login_page

driver = webdriver.Chrome()
driver.get(login_page.url)
time.sleep(2)
assert login_page.hasLoaded(driver)

login_page.username_input(driver).send_keys("standard_user")
login_page.password_input(driver).send_keys("secret_sauce")
time.sleep(2)
login_page.login_button(driver).click()

time.sleep(2)
assert driver.find_element(By.ID, "root")

driver.quit()
