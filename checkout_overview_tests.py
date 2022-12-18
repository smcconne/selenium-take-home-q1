# Python 3.9.7
from selenium import webdriver
from faker import Faker
import unittest
# Local imports
import login_page
import products_page
import cart_page
import checkout_page
import checkout_overview_page
import site_banner

class CheckoutOverviewPageTests(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get(login_page.url)
		login_page.attempt_login(self.driver, "standard_user", "secret_sauce")
		product = products_page.find_item_by_name(self.driver, "Bike Light")
		products_page.toggle_add_to_cart(self.driver, product).click()
		site_banner.cart_link(self.driver).click()
		cart_page.checkout_button(self.driver).click()
		self.fake = Faker()
		checkout_page.submit_user_info(self.driver, self.fake.first_name(), self.fake.last_name(), self.fake.postcode())
		self.assertTrue(checkout_overview_page.hasLoaded(self.driver))

	def test_correct_item_displayed_overview(self):
		self.assertTrue(checkout_overview_page.verify_item_name(self.driver, "Bike Light"))

	def test_exiting_overview_retains_cart(self):
		checkout_overview_page.cancel_button(self.driver).click()
		self.assertTrue(products_page.hasLoaded(self.driver))
		self.assertTrue(site_banner.cart_badge_exists(self.driver))

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
    unittest.main()