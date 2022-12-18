# Python 3.9.7
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.saucedemo.com/cart.html"

def hasLoaded(driver):
	try:
		WebDriverWait(driver, 10).until(
			lambda driver: cart_contents(driver)
		)
	except:
		return False
	else:
		return True
	
def cart_contents(driver):
	return driver.find_element(By.CLASS_NAME, "cart_contents_container")
	
def continue_shopping_button(driver):
	return driver.find_element(By.CSS_SELECTOR, "button#continue-shopping")
	
def checkout_button(driver):
	return driver.find_element(By.CSS_SELECTOR, "button#checkout")
	
def checkout_button_exists(driver):
	# An assert on this list will be false if no results are returned
	return driver.find_elements(By.CSS_SELECTOR, "button#checkout")
	
def find_item_by_name(driver, search):
	item_name_list = driver.find_element(By.CLASS_NAME, "inventory_item_name")
	
	return item_name_list.find_element(By.XPATH, "//*[text()[contains(.,\"" + search + "\")]]//ancestor::div[@class = \"cart_item\"]")
	
def remove_from_cart(driver, item):
	# item: an inventory item returned by find_item_by_name
	return item.find_element(By.CSS_SELECTOR, "button.cart_button")