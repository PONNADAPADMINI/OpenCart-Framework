from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver # 1. Add this import for suggestions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.base_page import BasePage



class Login_Page(BasePage):

    def __init__(self, driver: WebDriver):
        # 1. Start the Base Engine (Syncs the Driver & Wait)
        super().__init__(driver)

    #Locatores
    LOGIN_INPUT=(By.CSS_SELECTOR,"#input-email")
    PASSWORD_INPUT=(By.CSS_SELECTOR,'#input-password')
    LOGIN_BUTTON=(By.XPATH,"//input[@value='Login']")
    ERROR_MESSAGE=(By.XPATH,"//div[contains(@class,'alert-danger')]")
    ACCOUNT_PAGE_TEXT=(
        By.XPATH,"(//div[@id='content']//h2[normalize-space()='My Affiliate Account'])"
                    )

    def set_login_email(self,email):
        self.type_text(self.LOGIN_INPUT,email)

    def set_login_password(self,password):
        self.type_text(self.PASSWORD_INPUT,password)

    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)

    def get_Login_error_message(self):
        self.get_element_text(self.ERROR_MESSAGE)


    def verify_Login(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(self.ACCOUNT_PAGE_TEXT))
            return element.is_displayed()
        except:
            return False
