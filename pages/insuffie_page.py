from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class InsufficientPrivileges:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)
        self.click_here_button_locator = (
            By.XPATH,
            "//a[@href='/visualforce/session?url=https%3A%2F%2Fdream-saas-8002.lightning.force.com%2Flightning%2Fpage%2Fhome' and text()='here']"
        )

    def click_here_button(self):
        try:
            button = self.wait.until(EC.element_to_be_clickable(self.click_here_button_locator))
            button.click()
            time.sleep(3)
        except Exception as e:
            print(f"Could not click button: {e}")
