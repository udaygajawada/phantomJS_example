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
		results = self.driver.find_element_by_id("search-results-content");
		data = results.find_elements_by_tag_name("td")
		l_data = len(data)
		num_of_rows = int(l_data/6);
		count1 = 0
		count2 = 5
		for i in range(0,num_of_rows):
			print("***************************************************")
			print("job : "+ str(i+1) +"\n")			
			for data1 in data[count1:count2]:
				print(data1.text)
			count1 = count2 + 1
			count2 = count2 + 6
			print("\n")
		print("***************************************************")
		

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()
