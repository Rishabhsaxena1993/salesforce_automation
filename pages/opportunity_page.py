import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Opportunity():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)
        self.opportunities_button = (
            By.XPATH,  "(//span[@class='slds-truncate slds-m-right--xx-small' and @title='Opportunities'])[1]")
        self.oppty_new_button = (By.XPATH, "//button[contains(@class, 'slds-button') and @name='New' and text()='New']")
        self.oppty_name_input = (By.XPATH, "//input[contains(@id, 'input-') and @name='Name' and @type='text' and "
                                           "contains(@class, 'slds-input')]")
        self.close_date_locator = (By.XPATH, "//input[contains(@id, 'input-') and @name='CloseDate' and @type='text']")
        self.stage_combobox_locator = (By.XPATH, "//button[contains(@class, 'slds-combobox__input') and "
                                                 "@aria-label='Stage']")
        self.forecast_category_option_locator = (
            By.XPATH, "//button[contains(@class, 'slds-combobox__input') and @aria-label='Forecast Category']"
        )
        self.save_button_locator = (By.XPATH, "//button[@name='SaveEdit']")

    def click_opportunities_button(self):
        element = self.wait.until(EC.element_to_be_clickable(self.opportunities_button))
        element.click()
        time.sleep(4)

    def click_on_new_button(self):
        opptys = self.wait.until(EC.element_to_be_clickable(self.oppty_new_button))
        opptys.click()
        time.sleep(2)

    def oppty_name_field(self, oppty_name_enter):
        oppty_name = self.wait.until(EC.visibility_of_element_located(self.oppty_name_input))
        oppty_name.send_keys(oppty_name_enter)
        time.sleep(5)

    def close_date_picker(self, date_enter_method):
         oppty_date = self.wait.until(EC.visibility_of_element_located(self.close_date_locator))
         oppty_date.send_keys(date_enter_method)
         time.sleep(3)

    def select_stage_option(self, option_name):
        # Click combobox button to open dropdown (Stage)
        stage_combobox = self.wait.until(
            EC.element_to_be_clickable(self.stage_combobox_locator)
        )
        stage_combobox.click()
        time.sleep(5)  # Wait for dropdown animation, optional

        # Select the desired option from dropdown
        option_xpath = f"//lightning-base-combobox-item[@data-value='{option_name}']"
        option_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        )
        option_element.click()
        time.sleep(5)

    def select_forecast_category_option(self, option_name):
        forecast_category_button = self.wait.until(EC.element_to_be_clickable(self.forecast_category_option_locator))
        forecast_category_button.click()
        time.sleep(2)  # wait for dropdown animation
        option_xpath = f"//lightning-base-combobox-item[contains(@class, 'slds-listbox__option_plain') and @data-value='{option_name}']"
        option_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        option_element.click()
        time.sleep(2)

    def save_button_oppty_page(self):
        button_save = self.wait.until(EC.element_to_be_clickable(self.save_button_locator))
        button_save.click()
        time.sleep(2)