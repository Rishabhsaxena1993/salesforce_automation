from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class AccountsCreationModal():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

        self.account_name_input = (By.XPATH, "//input[contains(@id, 'input-') and @name='Name' and contains(@class, 'slds-input')]")
        self.save_button_locator = (By.XPATH, "//button[@name='SaveEdit']")

    def account_name_textfield(self, account_name1):
        name_input = self.wait.until(EC.visibility_of_element_located(self.account_name_input))
        name_input.send_keys(account_name1)

    def click_save_button(self):
        button_save = self.wait.until(EC.element_to_be_clickable(self.save_button_locator))
        button_save.click()
        time.sleep(5)
