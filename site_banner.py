# Python 3.9.7
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.saucedemo.com/inventory.html"

def hasLoaded(driver):
	try:
		WebDriverWait(driver, 10).until(
			lambda driver: primary_header(driver)
		)
	except:
		return False
	else:
		return True
	
def primary_header(driver):
	return driver.find_element(By.CLASS_NAME, "primary_header")
	
def cart_link(driver):
	return driver.find_element(By.CLASS_NAME, "shopping_cart_link")
	
def cart_badge_exists(driver):
	# An assert on this list will be false if no results are returned
	return driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
	