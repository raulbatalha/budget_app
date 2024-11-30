from pages.base_page import BasePage

class MainPage(BasePage):
    def click_on_transactions(self):
        transactions_button_locator = "//button[@id='transactions']"
        self.click(transactions_button_locator)
        
    def click_on_budgets(self):
        budgets_button_locator = "//button[@id='budgets']"
        self.click(budgets_button_locator)
