from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class PageLogIn:
    _instance = None
    URL = 'https://qa-v3-portal.screenmeet.com/'

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.salesforce_loc = (By.XPATH, "//div[text()='Salesforce']")
        self.salesforce_logo = (By.XPATH, "//img[@name='logo']")
        self.username_input_field = (By.XPATH, "//input[@id='username']")
        self.password_input_field = (By.XPATH, "//input[@id='password']")
        self.log_in_button = (By.XPATH, "//input[@id='Login']")

    def open(self):
        self.driver.get(self.URL)


    def select_salesforce(self):
        self.driver.find_element(*self.salesforce_loc).click()

    def is_salesforce_logo_displayed(self) -> bool:
        return self.driver.find_element(*self.salesforce_logo).is_displayed()

    def fill_in_username(self, username: str) -> None:
        self.driver.find_element(*self.username_input_field).send_keys(username)

    def fill_in_password(self, password: str) -> None:
        self.driver.find_element(*self.password_input_field).send_keys(password)

    def submit_log_in(self):
        self.driver.find_element(*self.log_in_button).click()



