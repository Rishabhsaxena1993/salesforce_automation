from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)  # Shorter wait for conditional element
        self.remind_me_later = (By.XPATH, "//a[text()='Remind Me Later']")

    def click_remind_me_later(self):
        try:
            button = self.wait.until(EC.element_to_be_clickable(self.remind_me_later))
            button.click()
        except TimeoutException:
            # Element not found or not clickable within timeout, silently continue
            pass
