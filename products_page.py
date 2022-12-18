# Python 3.9.7
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.saucedemo.com/inventory.html"

def hasLoaded(driver):
	try:
		WebDriverWait(driver, 10).until(
			lambda driver: inventory_list(driver)
		)
	except:
		return False
	else:
		return True
	
def inventory_list(driver):
	return driver.find_element(By.CLASS_NAME, "inventory_list")

def find_item_by_name(driver, search):
	item_name_list = inventory_list(driver).find_element(By.CLASS_NAME, "inventory_item_name")
	
	return item_name_list.find_element(By.XPATH, "//*[text()[contains(.,\"" + search + "\")]]//ancestor::div[@class = \"inventory_item\"]")
	
def toggle_add_to_cart(driver, item):
	# item: an inventory item returned by find_item_by_name
	return item.find_element(By.CSS_SELECTOR, "button.btn_inventory")