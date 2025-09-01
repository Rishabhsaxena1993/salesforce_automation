import pytest
import yaml
from pages.login_page import LoginPage

def get_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def test_user_success_login(driver):
    config = get_config()
    driver.get(config["url"])
    login_page = LoginPage(driver)
    login_page.login(config["username"], config["password"])


