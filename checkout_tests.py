# Python 3.9.7
from selenium import webdriver
from faker import Faker
import unittest
# Local imports
import login_page
import products_page
import cart_page
import checkout_page
import site_banner

class CheckoutPageTests(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get(login_page.url)
		login_page.attempt_login(self.driver, "standard_user", "secret_sauce")
		product = products_page.find_item_by_name(self.driver, "Bike Light")
		products_page.toggle_add_to_cart(self.driver, product).click()
		site_banner.cart_link(self.driver).click()
		cart_page.checkout_button(self.driver).click()
		self.assertTrue(checkout_page.hasLoaded(self.driver))
		self.fake = Faker()

	def test_error_no_first_name(self):
		checkout_page.submit_user_info(self.driver, "", self.fake.last_name(), self.fake.postcode())
		self.assertTrue(checkout_page.hasLoaded(self.driver))
		self.assertTrue(checkout_page.check_error_exists(self.driver))
		self.assertTrue(checkout_page.verify_error_message(self.driver, "First Name is required"))
		login_page.error_close_button(self.driver).click()
		self.assertFalse(checkout_page.check_error_exists(self.driver))
		
	def test_error_no_last_name(self):
		checkout_page.submit_user_info(self.driver, self.fake.first_name(), "", self.fake.postcode())
		self.assertTrue(checkout_page.hasLoaded(self.driver))
		self.assertTrue(checkout_page.check_error_exists(self.driver))
		self.assertTrue(checkout_page.verify_error_message(self.driver, "Last Name is required"))
		login_page.error_close_button(self.driver).click()
		self.assertFalse(checkout_page.check_error_exists(self.driver))
		
	def test_error_no_postal_code(self):
		checkout_page.submit_user_info(self.driver, self.fake.first_name(), self.fake.last_name(), "")
		self.assertTrue(checkout_page.hasLoaded(self.driver))
		self.assertTrue(checkout_page.check_error_exists(self.driver))
		self.assertTrue(checkout_page.verify_error_message(self.driver, "Postal Code is required"))
		login_page.error_close_button(self.driver).click()
		self.assertFalse(checkout_page.check_error_exists(self.driver))
		
	def test_cancel_retains_cart(self):
		checkout_page.cancel_button(self.driver).click()
		self.assertTrue(cart_page.hasLoaded(self.driver))
		self.assertTrue(site_banner.cart_badge_exists(self.driver))

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
    unittest.main()