from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver # 1. Add this import for suggestions
from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage



class Home_page(BasePage):

    def __init__(self, driver: WebDriver):
        # 1. Start the Base Engine (Syncs the Driver & Wait)
        super().__init__(driver)

    # ------------Locatores----------
    MY_ACCOUNT_MENU_DROPDOWN=(By.XPATH,"//a[@title='My Account']")
    REGISTER_BUTTON=(By.LINK_TEXT,"Register")
    LOGIN_BUTTON=(By.XPATH,"(//ul[@class='dropdown-menu dropdown-menu-right']//a)[2]")

    def click_myAccountTxt(self):
        self.click_element(self.MY_ACCOUNT_MENU_DROPDOWN)

    def click_dropdownOption_register(self):
        self.click_element(self.REGISTER_BUTTON)


    def click_dropdownOption_login(self):
        self.click_element(self.LOGIN_BUTTON)
