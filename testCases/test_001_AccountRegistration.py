import os
from pageObjects.Home_Page import Home_page
from pageObjects.AccountRegistrationPage import Account_Register
from utilities.readProperties import readconfig
from utilities.custom_Logger import LogGen
import pytest

from utilities.randomString import random_string_generator


class Test_Account_Reg():
    base_url=readconfig.getApplicationUrl()
    test_password = readconfig.getPassword()

    logger = LogGen.logGen()

    @pytest.mark.regression
    def test_account_reg(self,setup):
        self.logger.info("**** test_001_AccountRegistration started *** ")
        self.driver=setup
        self.logger.info("**** Launching Test Application ***")
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        #HomePageObject
        self.hp=Home_page(self.driver)
        self.hp.click_myAccountTxt()
        self.hp.click_dropdownOption_register()

    #RegisterpageObject
        self.logger.info("**** Navigated to Registration Page & Filling the details *** ")
        self.regPage=Account_Register(self.driver)
        self.regPage.set_firstName("khaja")
        self.regPage.set_lastname("QsSk")
        #Random Email Generatore ro Avoid Duplication
        self.email=random_string_generator()+"@yopmail.com"
        self.regPage.set_email(self.email)

        self.regPage.set_telephone("8153264120")
        self.regPage.set_password("White@456")
        self.regPage.set_confirm_password("White@45")
        password=self.regPage.get_password()
        cnf_pwd=self.regPage.get_confirm_password()
        assert password==cnf_pwd, f"Assertion failed with Type '{password}',confirmed'{cnf_pwd}'"
        print("Passwords matched successfully!")
        self.logger.info("**** Password-Matched Successfully *** ")
        self.regPage.select_newsletter_options("No")
        self.regPage.agree_privacy_policy()
        submit=self.regPage.submit_registration()

#Account Registration Validation
        message=self.regPage.confirm_message()
        if message=="Your Account Has Been Created!":
            self.logger.info("Account Registration Completed successfully")
            print("Account creation is Successful")
            assert True
        else:
            self.logger.info("Account Registration Have Failed to Reach Confirmation Page")
            print("Account Registration Failed")
            assert False
            # screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            # os.makedirs(screenshot_dir, exist_ok=True)
            # screenshot_path = os.path.join(screenshot_dir, "test_account_reg.png")
            # self.driver.save_screenshot(screenshot_path)


