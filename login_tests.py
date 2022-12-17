from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import unittest
import time
# Local imports
import login_page
import products_page

class LoginTests(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.fake = Faker()
		self.driver.get(login_page.url)
		self.assertTrue(login_page.hasLoaded(self.driver))

	def test_login_success(self):
		login_page.attempt_login(self.driver, "standard_user", "secret_sauce")
		self.assertTrue(products_page.hasLoaded(self.driver))

	def test_login_failure(self):
		login_page.attempt_login(self.driver, self.fake.email(), self.fake.text())
		self.assertTrue(login_page.check_error_exists(self.driver))
		self.assertTrue(login_page.verify_error_message(self.driver, "Username and password do not match any user"))
		login_page.error_close_button(self.driver).click()
		self.assertFalse(login_page.check_error_exists(self.driver))

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
    unittest.main()