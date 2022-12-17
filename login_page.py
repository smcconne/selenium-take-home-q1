from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.saucedemo.com/"

def hasLoaded(driver):
	try:
		WebDriverWait(driver, 10).until(
			lambda driver: login_button(driver)
		)
	except:
		return False
	else:
		return True
	
def username_input(driver):
	return driver.find_element(By.ID, "user-name")

def password_input(driver):
	return driver.find_element(By.ID, "password")
	
def login_button(driver):
	return driver.find_element(By.ID, "login-button")
	
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
	
def attempt_login(driver, username, password):
	username_input(driver).send_keys(username)
	password_input(driver).send_keys(password)
	login_button(driver).click()