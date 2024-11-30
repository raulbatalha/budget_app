import time
from selenium.webdriver.common.by import By

def capture_screenshot(driver, test_name, directory='tests/evidencias'):
    timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_path = f"{directory}/{test_name}_{timestamp}.png"
    driver.get_screenshot_as_file(screenshot_path)
    print(f"Screenshot saved to: {screenshot_path}")
    return screenshot_path
