from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
import threading

def initialize_driver(platform, device_name, app_path, app_package=None, app_activity=None):
    desired_caps = None
    if platform.lower() == 'android':
        desired_caps = UiAutomator2Options()
        desired_caps.platform_name = 'Android'
        desired_caps.device_name = device_name
        desired_caps.app = app_path
        desired_caps.app_package = app_package
        desired_caps.app_activity = app_activity
        desired_caps.automation_name = 'UiAutomator2'
    elif platform.lower() == 'ios':
        desired_caps = XCUITestOptions()
        desired_caps.platform_name = 'iOS'
        desired_caps.device_name = device_name
        desired_caps.app = app_path
        desired_caps.automation_name = 'XCUITest'

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=desired_caps)
    return driver

def create_driver_for_multiple_devices(devices):
    drivers = []
    threads = []
    for device in devices:
        thread = threading.Thread(target=lambda: drivers.append(initialize_driver(*device)))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return drivers
