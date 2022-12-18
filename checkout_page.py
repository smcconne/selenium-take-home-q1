# Python 3.9.7
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.saucedemo.com/checkout-step-one.html"

def hasLoaded(driver):
	try:
		WebDriverWait(driver, 10).until(
			lambda driver: checkout_info(driver)
		)
	except:
		return False
	else:
		return True
	
def checkout_info(driver):
	return driver.find_element(By.CLASS_NAME, "checkout_info")
	
def cancel_button(driver):
	return driver.find_element(By.CSS_SELECTOR, "button#cancel")
	
def continue_button(driver):
	return driver.find_element(By.CSS_SELECTOR, "input#continue")
	
def first_name_input(driver):
	return driver.find_element(By.CSS_SELECTOR, "input#first-name")
	
def last_name_input(driver):
	return driver.find_element(By.CSS_SELECTOR, "input#last-name")
	
def postal_code_input(driver):
	return driver.find_element(By.CSS_SELECTOR, "input#postal-code")
	
def submit_user_info(driver, firstname, lastname, postalcode):
	first_name_input(driver).send_keys(firstname)
	last_name_input(driver).send_keys(lastname)
	postal_code_input(driver).send_keys(postalcode)
	continue_button(driver).click()