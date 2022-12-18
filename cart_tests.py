# Python 3.9.7
from selenium import webdriver
import unittest
# Local imports
import login_page
import products_page
import cart_page
import site_banner

class CartPageTests(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get(login_page.url)
		login_page.attempt_login(self.driver, "standard_user", "secret_sauce")
		product = products_page.find_item_by_name(self.driver, "Bike Light")
		products_page.toggle_add_to_cart(self.driver, product).click()
		site_banner.cart_link(self.driver).click()
		self.assertTrue(cart_page.hasLoaded(self.driver))
		self.assertTrue(site_banner.cart_badge_exists(self.driver))

	def test_remove_from_cart(self):
		product = cart_page.find_item_by_name(self.driver, "Bike Light")
		cart_page.remove_from_cart(self.driver, product).click()
		self.assertFalse(site_banner.cart_badge_exists(self.driver))
		
	def test_continue_shopping_retains_cart(self):
		cart_page.continue_shopping_button(self.driver).click()
		self.assertTrue(products_page.hasLoaded(self.driver))
		self.assertTrue(site_banner.cart_badge_exists(self.driver))

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
    unittest.main()