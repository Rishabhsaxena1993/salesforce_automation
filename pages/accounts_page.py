from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class AccountsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

        self.account_button_locator_1 = (
            By.XPATH,
            "(//span[contains(@class, 'appItemLabel') and text()='Accounts'])"
        )
        self.account_button_locator_2 = (
            By.XPATH,
            "(//span[contains(@class,'slds-truncate') and text()='Accounts'])[2]"
        )
        self.new_button_locator = (By.XPATH, "//div[@title='New']")

        # Agar yeh chahiye toh define karo, warna method se hata do
        # self.select_account_link_after_account_created = (By.XPATH, "<locator xpath>")

    def click_first_accounts(self):
        element = self.wait.until(EC.element_to_be_clickable(self.account_button_locator_1))
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(10)

    def click_second_accounts(self):
        element = self.wait.until(EC.element_to_be_clickable(self.account_button_locator_2))
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(5)

    def click_on_new_button(self):
        element = self.wait.until(EC.element_to_be_clickable(self.new_button_locator))
        element.click()
        time.sleep(5)

    # Agar is method ka use karna hai toh
    # def click_account_link_after_account_created(self):
    #     element = self.wait.until(
    #         EC.element_to_be_clickable(self.select_account_link_after_account_created)
    #     )
    #     element.click()
    #     time.sleep(2)

    def click_account_by_name(self, account_name):
        # Dynamic XPath with account_name
        account_link_xpath = f"//a[@title='{account_name}']"
        account_link_locator = (By.XPATH, account_link_xpath)
        element = self.wait.until(EC.element_to_be_clickable(account_link_locator))
        element.click()
        time.sleep(2)
