import unittest
from utils.appium_config import create_driver_for_multiple_devices
from utils.data_loader import load_test_data
from utils.screenshot_util import capture_screenshot
from pages.main_page import MainPage

class MultiDeviceTests(unittest.TestCase):
    def setUp(self):
        devices_config = load_test_data('config/app_config.json')['devices']
        self.drivers = create_driver_for_multiple_devices(devices_config)

    def test_transactions_on_multiple_devices(self):
        for driver in self.drivers:
            main_page = MainPage(driver)
            main_page.click_on_transactions()
            capture_screenshot(driver, 'transactions_test')

    def test_budgets_on_multiple_devices(self):
        for driver in self.drivers:
            main_page = MainPage(driver)
            main_page.click_on_budgets()
            capture_screenshot(driver, 'budgets_test')

    def tearDown(self):
        for driver in self.drivers:
            driver.quit()

if __name__ == '__main__':
    unittest.main()
