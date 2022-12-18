# Python 3.9.7
from selenium import webdriver
import unittest
# Local imports
import login_page
import products_page
import site_banner

class ProductsPageTests(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get(login_page.url)
		self.assertTrue(login_page.hasLoaded(self.driver))
		login_page.attempt_login(self.driver, "standard_user", "secret_sauce")
		self.assertTrue(products_page.hasLoaded(self.driver))

	def test_add_and_remove_from_cart(self):
		self.assertFalse(site_banner.cart_badge_exists(self.driver))
		product = products_page.find_item_by_name(self.driver, "Bike Light")
		products_page.toggle_add_to_cart(self.driver, product).click()
		self.assertTrue(site_banner.cart_badge_exists(self.driver))
		products_page.toggle_add_to_cart(self.driver, product).click()
		self.assertFalse(site_banner.cart_badge_exists(self.driver))

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
    unittest.main()