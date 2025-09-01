from pages.account_create_modal import AccountsCreationModal
from pages.accounts_page import AccountsPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.opportunity_page import Opportunity
import yaml


def get_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)


def test_user_success_login(driver):
    config = get_config()
    driver.get(config["url"])

    login_page = LoginPage(driver)
    account_page = AccountsPage(driver)
    accounts_creationmodal = AccountsCreationModal(driver)
    opportunityaa = Opportunity(driver)

    login_page.login(config["username"], config["password"])

    dashboard_page = DashboardPage(driver)
    dashboard_page.click_remind_me_later()


    account_page.click_first_accounts()
    account_page.click_second_accounts()
    account_page.click_on_new_button()

    accounts_creationmodal.account_name_textfield("Test10")
    accounts_creationmodal.click_save_button()

    account_page.click_second_accounts()
    account_page.click_account_by_name("Test10")  # Yahan "Test1" badal ke dynamic account name dena hai

    opportunityaa.click_opportunities_button()
    opportunityaa.click_on_new_button()

