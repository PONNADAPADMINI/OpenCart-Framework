
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver # 1. Add this import for suggestions
from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage


class AccountPage(BasePage):

    def __init__(self, driver: WebDriver):
        # 1. Start the Base Engine (Syncs the Driver & Wait)
        super().__init__(driver)

    ACCOUNT_TEXT = (By.XPATH, "//span[contains(normalize-space(),'My Account')]")
    LOGOUT_BUTTON = (By.XPATH, "//ul[contains(@class,'dropdown-menu-right')]//li//a")
    def click_myAccountTxt(self):
        self.click_element(self.ACCOUNT_TEXT)

    def click_logout_Button(self):
        ddOptions = self.get_multiple_elements(self.LOGOUT_BUTTON)

        for option in ddOptions:
            actual_text = option.text.strip()
            if actual_text == "Logout":
                option.click()
                return actual_text
        assert False, "Logout button not found in dropdown"