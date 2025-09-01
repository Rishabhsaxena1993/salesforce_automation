import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Opportunity():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)
        self.opportunities_button = (
            By.XPATH,  "(//span[@class='slds-truncate slds-m-right--xx-small' and @title='Opportunities'])[1]"
        )
        self.oppty_name_button = (By.XPATH, "//button[contains(@class, 'slds-button') and @name='New' and text()='New']")

    def click_opportunities_button(self):
        element = self.wait.until(EC.element_to_be_clickable(self.opportunities_button))
        element.click()
        time.sleep(4)

    def click_on_new_button(self):
        opptys = self.wait.until(EC.element_to_be_clickable(self.oppty_name_button))
        opptys.click()
        time.sleep(2)
