# Python 3.9.7
import unittest
# Local imports
import login_tests
import products_tests
import cart_tests
import checkout_tests
import checkout_overview_tests
import checkout_complete_tests

# Aggregate all tests into one suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()
suite.addTests(loader.loadTestsFromModule(login_tests))
suite.addTests(loader.loadTestsFromModule(products_tests))
suite.addTests(loader.loadTestsFromModule(cart_tests))
suite.addTests(loader.loadTestsFromModule(checkout_tests))
suite.addTests(loader.loadTestsFromModule(checkout_overview_tests))
suite.addTests(loader.loadTestsFromModule(checkout_complete_tests))

# Pass suite to runner
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)