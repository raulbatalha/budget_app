from pages.base_page import BasePage

class IntroPage(BasePage):
    def click_skip_button(self):
        skip_button_locator = "//button[@id='skip']"
        self.click(skip_button_locator)
