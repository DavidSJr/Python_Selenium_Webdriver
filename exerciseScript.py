from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by  import By

import unittest

import time


class LeatherBack(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://travelingtony.weebly.com")
        #driver.implicitly_wait(15)
    
    
    def test_LeatherBack(self):
        searchMenuLocator = "//input[@name=q]"
        nameFieldLocator   = "//input[contains(@name, 'q')]"
        searchMenuElement = WebDriverWait(driver, 10).\
                             #until(lambda driver: driver.find_element_by_xpath(searchMenuLocator))
        searchMenuElement.click()
        nameFieldElement   = WebDriverWait(driver, 10).\
                             until(lambda driver: driver.find_element_by_xpath(nameFieldLocator))
        nameFieldElement.send_keys("leatherback")


        time.sleep(6)

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()