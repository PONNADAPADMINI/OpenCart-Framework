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
        self.hp=Home_page(self.driver)
        self.hp.click_myAccountTxt()
        self.hp.click_dropdownOption_register()

        self.logger.info("**** Navigated to Registration Page & Filling the details *** ")
        self.regPage=Account_Register(self.driver)
        self.regPage.set_firstName("Test_user")
        self.regPage.set_lastname("QsSk")
        self.email=random_string_generator()+"@yopmail.com"
        self.regPage.set_email(self.email)
        self.regPage.set_telephone("0239839000")
        self.regPage.set_password("Test@456")
        self.regPage.set_confirm_password("Test@456")
        password=self.regPage.get_password()
        cnf_pwd=self.regPage.get_confirm_password()
        assert password==cnf_pwd, f"Assertion failed with Type '{password}',confirmed'{cnf_pwd}'"
        print("Passwords matched successfully!")
        self.logger.info("**** Password-Matched Successfully *** ")
        self.regPage.select_newsletter_options("No")
        self.regPage.agree_privacy_policy()
        self.regPage.submit_registration()

        self.logger.info("**** Validateing the account Page navigation *** ")
        current_url = self.driver.current_url
        print(current_url)
        if "route=account/success" in current_url:
            self.logger.info(f"Navigated Succesfully to : {current_url}")
            assert True
        else:
            self.logger.error(f"Navigation failed - still on Registration page {current_url}")
            assert False,"Signup Failed"

#Account Registration Validation
        message=self.regPage.confirm_message()
        if message=="Your Account Has Been Created!":
            self.logger.info("Account Registration Completed is successfull")
            assert True
        else:
            self.logger.info("Account Registration Have Failed at Confirmation Page")
            assert False



