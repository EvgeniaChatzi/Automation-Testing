import unittest
import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class TestCaseDemo(unittest.TestCase):

    def setUp(self):

        driverLocation = "D:\\Projects\\Dev\\LearnPython\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        self.driver = webdriver.Chrome(driverLocation)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_navigation(self):


        baseURL = "URL"
        self.driver.get(baseURL)

        time.sleep(2)
        # Scroll down
        self.driver.execute_script("window.scrollBy(0, 1600);")

        time.sleep(2)

        self.driver.find_element(By.CSS_SELECTOR, ".js-scroll-down").click()

        time.sleep(2)

        # Scroll down
        self.driver.execute_script("window.scrollBy(0, 7000);")

        time.sleep(2)

        self.driver.execute_script("window.scrollBy(0, -800);")

        time.sleep(2)

        countryfield = self.driver.find_element(By.LINK_TEXT, "Junior Software Tester")
        countryfield.click()

        time.sleep(2)

        self.driver.find_element(By.LINK_TEXT, "APPLY FOR THIS JOB").click()
        time.sleep(2)

        fullNameField = self.driver.find_element(By.NAME, "name")
        fullNameField.send_keys("Evgenia Chatzi")
        time.sleep(2)

        fullNameField = self.driver.find_element(By.NAME, "email")
        fullNameField.send_keys("chatzievgenia7@gmail.com")
        time.sleep(2)

        fullNameField = self.driver.find_element(By.NAME, "phone")
        fullNameField.send_keys("99179330")
        time.sleep(2)


if __name__== '__main__':
    unittest.main(verbosity=2)



