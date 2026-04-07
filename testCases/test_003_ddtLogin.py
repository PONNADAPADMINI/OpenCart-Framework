import os.path

from pageObjects.Home_Page import Home_page
from pageObjects.login_Page import Login_Page
from utilities.custom_Logger import LogGen
from utilities.readProperties import readconfig
from pageObjects.Account_Page import AccountPage
from utilities import XLUtils
import pytest



class Test_loginDDT():

    logger=LogGen.logGen()
    base_url=readconfig.getApplicationUrl()

    @pytest.mark.sanity
    def test_LoginDDT(self,setup):
        self.logger.info("-------->>>>  Starting test_Login_DDT_Test <<<<<<< ---------")
        test_file = os.path.abspath(os.path.curdir) + r"\testData\Opencart_LoginData.xlsx"
        self.rows=XLUtils.getRowCount(test_file,"Sheet1")
        print( "Length of row count is : - ",self.rows)
        lst_status = []

        self.driver=setup
        self.driver.get(self.base_url)
        self.Hp=Home_page(self.driver)
        self.Lp=Login_Page(self.driver)
        self.Ap=AccountPage(self.driver)


        for r in range(2,self.rows+1):
            # 1. Reset state
            self.driver.get(self.base_url)
            # 2. Navigate
            self.Hp.click_myAccountTxt()
            self.Hp.click_dropdownOption_login()

            # 3. Read Data
            self.email=XLUtils.readData(test_file,"Sheet1",r,1)
            self.password=XLUtils.readData(test_file,"Sheet1",r,2)
            self.expected=XLUtils.readData(test_file,"Sheet1",r,3)
            # 4. Action
            self.Lp.set_login_email(self.email)
            self.Lp.set_login_password(self.password)
            self.Lp.click_login_button()


            # 5. Validation
            self.postLogin_Page =self.Lp.verify_Login()
            # TC"1" :- Test Login with Valid data
            if self.expected=="Valid":
                if self.postLogin_Page==True:
                    lst_status.append("PASS")
                    self.Ap.click_myAccountTxt()
                    self.Ap.click_logout_Button()
                else:
                    lst_status.append("FAIL")

            # TC"2" :- Test Login with In-Valid data
            elif self.expected=="Invalid":
                if self.postLogin_Page==True:
                    lst_status.append("FAIL")
                    self.Ap.click_myAccountTxt()
                    self.Ap.click_logout_Button()
                else:
                    lst_status.append("PASS")

        print(lst_status)
        if "FAIL" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info(("---------------End of test driven Testing-----------------------"))

















