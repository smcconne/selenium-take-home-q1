# Python 3.9.7
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
	
def attempt_login(driver, username, password):
	username_input(driver).send_keys(username)
	password_input(driver).send_keys(password)
	login_button(driver).click()