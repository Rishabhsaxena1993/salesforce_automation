from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10 second wait

        # Locators
        self.username_input = (By.XPATH, "//input[@id='username']")
        self.password_input = (By.XPATH, "//input[@id='password']")
        self.login_button = (By.XPATH, "//input[@id='Login']")

    # Page actions
    def enter_username(self, username):
        username_field = self.wait.until(EC.visibility_of_element_located(self.username_input))
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(EC.visibility_of_element_located(self.password_input))
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self.login_button))
        login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
