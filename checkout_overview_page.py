# Python 3.9.7
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.saucedemo.com/checkout-step-two.html"

def hasLoaded(driver):
	try:
		WebDriverWait(driver, 10).until(
			lambda driver: checkout_summary(driver)
		)
	except:
		return False
	else:
		return True
	
def checkout_summary(driver):
	return driver.find_element(By.CLASS_NAME, "checkout_summary_container")
	
def cancel_button(driver):
	return driver.find_element(By.CSS_SELECTOR, "button#cancel")
	
def finish_button(driver):
	return driver.find_element(By.CSS_SELECTOR, "button#finish")
	
def find_item_by_name(driver, search):
	item_name_list = driver.find_element(By.CLASS_NAME, "inventory_item_name")
	
	return item_name_list.find_element(By.XPATH, "//*[text()[contains(.,\"" + search + "\")]]//ancestor::div[@class = \"cart_item\"]")