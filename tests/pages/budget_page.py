from pages.base_page import BasePage

class BudgetPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def create_new_budget(self, budget_name, amount):
        budget_name_locator = "//input[@id='budget_name']"
        amount_locator = "//input[@id='budget_amount']"
        submit_button_locator = "//button[@id='submit_budget']"
        
        self.find_element(budget_name_locator).send_keys(budget_name)
        self.find_element(amount_locator).send_keys(amount)
        self.click(submit_button_locator)
        
    def get_budget_details(self):
        budget_details_locator = "//div[@id='budget_details']"
        return self.find_element(budget_details_locator).text
