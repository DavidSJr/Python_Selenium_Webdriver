# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class NavigatetoHQ(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://docs.seleniumhq.org/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_navigateto_h_q(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        for i in range(60):
            try:
                if "Selenium - Web Browser Automation" == driver.title: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_link_text("Download").click()
        self.assertEqual("Downloads", driver.title)
        driver.find_element_by_link_text("Documentation").click()
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys("webdriver")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_xpath("//div[@id='cse']/div/div/div/div[5]/div[2]/div/div/div/div/table/tbody/tr/td[2]/div").click()
        # Warning: assertTextPresent may require manual changes
        self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*$")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
