from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver

class BasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def click(self, locator):
        element = self.driver.find_element(MobileBy.XPATH, locator)
        element.click()

    def find_element(self, locator):
        return self.driver.find_element(MobileBy.XPATH, locator)
