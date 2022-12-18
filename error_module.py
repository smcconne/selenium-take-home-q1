# Python 3.9.7
from selenium import webdriver
from selenium.webdriver.common.by import By
	
def check_error_exists(driver):
	# An assert on this list will be false if no results are returned
	return driver.find_elements(By.CSS_SELECTOR, "div.error")
	
def error(driver):
	return driver.find_element(By.CSS_SELECTOR, "div.error")
	
def verify_error_message(driver, message):
	# An assert on this list will be false if no results are returned
	return error(driver).find_elements(By.XPATH, "//h3[contains(., \"" + message + "\")]")
	
def error_close_button(driver):
	return error(driver).find_element(By.CLASS_NAME, "error-button")