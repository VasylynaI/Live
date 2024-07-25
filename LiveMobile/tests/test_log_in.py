import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from LiveMobile.pages.page_log_in import PageLogIn
import time


@pytest.mark.usefixtures("chrome")
class TestLogIn:
    driver: WebDriver
    page_log_in: PageLogIn

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page_log_in = PageLogIn(self.driver)
        self.page_log_in.open()

    def test_select_salesforce(self):
        self.page_log_in.select_salesforce()
        time.sleep(5)
        assert self.page_log_in.is_salesforce_logo_displayed()
        time.sleep(5)

    def test_fill_in_username(self):
        username = '...'
        self.page_log_in.fill_in_username(username)
        actual_username_value = self.driver.find_element(*self.page_log_in.username_input_field).get_attribute('value')
        assert actual_username_value == username

    def test_fill_in_password(self):
        password = '...'
        self.page_log_in.fill_in_password(password)
        actual_password_value = self.driver.find_element(*self.page_log_in.password_input_field).get_attribute('value')
        assert actual_password_value == password

