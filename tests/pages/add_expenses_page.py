from pages.base_page import BasePage

class AddExpensesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def input_expense_details(self, expense_name, amount):
        expense_name_locator = "//input[@id='expense_name']"
        amount_locator = "//input[@id='expense_amount']"
        submit_button_locator = "//button[@id='submit_expense']"
        
        self.find_element(expense_name_locator).send_keys(expense_name)
        self.find_element(amount_locator).send_keys(amount)
        self.click(submit_button_locator)
        
    def confirm_expense_creation(self):
        confirmation_message_locator = "//div[@id='expense_confirmation']"
        return self.find_element(confirmation_message_locator).text
