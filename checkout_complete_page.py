# Python 3.9.7
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.saucedemo.com/checkout-complete.html"

def hasLoaded(driver):
	try:
		WebDriverWait(driver, 10).until(
			lambda driver: checkout_complete(driver)
		)
	except:
		return False
	else:
		return True
	
def checkout_complete(driver):
	return driver.find_element(By.CLASS_NAME, "checkout_complete_container")
	
def back_home_button(driver):
	return driver.find_element(By.CSS_SELECTOR, "button#back-to-products")