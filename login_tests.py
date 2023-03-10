# Python 3.9.7
from selenium import webdriver
from faker import Faker
import unittest
# Local imports
import login_page
import products_page
import error_module

class LoginPageTests(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get(login_page.url)
		self.assertTrue(login_page.hasLoaded(self.driver))

	def test_login_success(self):
		login_page.attempt_login(self.driver, "standard_user", "secret_sauce")
		self.assertTrue(products_page.hasLoaded(self.driver))

	def test_login_invalid_credentials(self):
		self.fake = Faker()
		login_page.attempt_login(self.driver, self.fake.user_name(), self.fake.text())
		self.assertTrue(error_module.check_error_exists(self.driver))
		self.assertTrue(error_module.verify_error_message(self.driver, "Username and password do not match any user"))
		
	def test_error_disappears_when_closed(self):
		self.fake = Faker()
		login_page.attempt_login(self.driver, self.fake.user_name(), self.fake.text())
		self.assertTrue(error_module.check_error_exists(self.driver))
		error_module.error_close_button(self.driver).click()
		self.assertFalse(error_module.check_error_exists(self.driver))

	def tearDown(self):
		self.driver.quit()
		
class UnauthorizedTests(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get(products_page.url)
		
	def test_unauthorized_access(self):
		self.assertTrue(login_page.hasLoaded(self.driver))
		self.assertTrue(error_module.check_error_exists(self.driver))
		self.assertTrue(error_module.verify_error_message(self.driver, "You can only access '/inventory.html' when you are logged in."))
		
	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
    unittest.main()