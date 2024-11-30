from pages.base_page import BasePage

class AddBudgetPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def input_budget_details(self, budget_name, amount):
        budget_name_locator = "//input[@id='budget_name']"
        amount_locator = "//input[@id='budget_amount']"
        submit_button_locator = "//button[@id='submit_budget']"
        
        self.find_element(budget_name_locator).send_keys(budget_name)
        self.find_element(amount_locator).send_keys(amount)
        self.click(submit_button_locator)
        
    def confirm_budget_creation(self):
        confirmation_message_locator = "//div[@id='budget_confirmation']"
        return self.find_element(confirmation_message_locator).text
