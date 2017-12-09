import unittest
import time
from selenium import webdriver

class TestOne(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.PhantomJS()
		self.driver.set_window_size(1120, 550)

	def test_url(self):
		self.driver.get("http://jobs.kent.edu/cw/en-us/listing/")
		self.driver.find_element_by_id('search-keyword').send_keys("chemistry")
		time.sleep(5)
		self.assertIn("http://jobs.kent.edu/cw/en-us/search/?search-keyword=chemistry", self.driver.current_url)

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()
