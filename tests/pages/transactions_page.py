from pages.base_page import BasePage

class TransactionsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def add_new_transaction(self, amount, description):
        amount_locator = "//input[@id='transaction_amount']"
        description_locator = "//input[@id='transaction_description']"
        submit_button_locator = "//button[@id='submit_transaction']"
        
        self.find_element(amount_locator).send_keys(amount)
        self.find_element(description_locator).send_keys(description)
        self.click(submit_button_locator)
        
    def get_transaction_details(self):
        transaction_details_locator = "//div[@id='transaction_details']"
        return self.find_element(transaction_details_locator).text
