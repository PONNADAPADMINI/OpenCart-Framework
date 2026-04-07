import pytest
from pageObjects.Home_Page import Home_page
from pageObjects.login_Page import Login_Page
from utilities.readProperties import readconfig # Corrected import path
from utilities.custom_Logger import LogGen # Corrected import path
from selenium.webdriver.remote.webdriver import WebDriver # 1. Add this import for suggestions
from pageObjects.Account_Page import AccountPage


class Test_login():
    base_url=readconfig.getApplicationUrl()
    email=readconfig.getEmail()
    password=readconfig.getPassword()
    logger=LogGen.logGen()

    @pytest.mark.sanity
    def test_login(self,setup):

        self.logger.info("----->>> test_002_Login Started Executing <<<------")
        self.driver = setup
        self.driver.get(self.base_url)
        self.hp=Home_page(self.driver)
        self.Ap=AccountPage(self.driver)

        self.logger.info("----->>> Navigating to Login Page <<<------")
        self.hp.click_myAccountTxt()
        self.hp.click_dropdownOption_login()

        self.logger.info("----->>> Entering the Login Credentials <<<------")
        self.login_page=Login_Page(self.driver)
        self.login_page.set_login_email(self.email)
        self.login_page.set_login_password(self.password)
        self.login_page.click_login_button()
        self.target_page=self.login_page.verify_Login()
        if self.target_page==True:
            assert True
        else:
            assert False
        self.Ap.click_myAccountTxt()
        self.Ap.click_logout_Button()
        self.logger.info("----->>> End of test_002_Login Test <<<------")


