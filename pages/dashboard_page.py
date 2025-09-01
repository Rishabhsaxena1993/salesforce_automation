from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.remind_me_later = (By.XPATH, "//a[text()='Remind Me Later']")

    def click_remind_me_later(self):
        button = self.wait.until(EC.visibility_of_element_located(self.remind_me_later))
        button.click()
