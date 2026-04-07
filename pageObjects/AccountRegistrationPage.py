from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pageObjects.base_page import BasePage


class Account_Register(BasePage):

    def __init__(self, driver: WebDriver):
        # 1. Start the Base Engine (Syncs the Driver & Wait)
        super().__init__(driver)

    #-Locatores ----

    FIRST_NAME_INPUT=(By.CSS_SELECTOR,"#input-firstname")
    LAST_NAME_INPUT=(By.XPATH,"//input[@id='input-lastname']")
    EMAIL_INPUT=(By.CSS_SELECTOR,"#input-email")
    TELEPHONE_INPUT=(By.NAME,"telephone")
    PASSWORD_INPUT=(By.CSS_SELECTOR,"#input-password")
    CONFIRM_PASSWORD_INPUT=(By.XPATH,"//input[@name='confirm']")
    SUBSCRIBE_OPTIONS_TEXT=(By.XPATH,"(//label[@class='radio-inline'])")
    SUBSCRIBE_RADIO_BUTTONS=(By.XPATH,"//label[@class='radio-inline']//input")
    PRIVACY_POLICY_CHECKBOX=(By.XPATH,"//input[@name='agree']")
    CONTINUE_BUTTON=(By.CSS_SELECTOR,".btn.btn-primary")
    CONFIRM_MESSAGE_TXT=(By.XPATH,"//div[@id='content']//h1")



    def set_firstName(self,first_name):
        self.type_text(self.FIRST_NAME_INPUT,first_name)

    def set_lastname(self,last_name):
        self.type_text(self.LAST_NAME_INPUT, last_name)

    def set_email(self,email):
        self.type_text(self.EMAIL_INPUT, email)

    def set_telephone(self,number):
        self.type_text(self.TELEPHONE_INPUT,number)

    def set_password(self,password):
        self.type_text(self.PASSWORD_INPUT,password)

    def set_confirm_password(self,cnfrm_password):
        self.type_text(self.CONFIRM_PASSWORD_INPUT,cnfrm_password)

    def get_password(self):
        return self.get_attribute_value(self.PASSWORD_INPUT)

    def get_confirm_password(self):
        return self.get_attribute_value(self.CONFIRM_PASSWORD_INPUT)

    def select_newsletter_options(self ,choices):
        options=self.get_multiple_elements(self.SUBSCRIBE_OPTIONS_TEXT)

        for option in options:
            if option.text.strip() ==choices:
                option.click()
                break

    def agree_privacy_policy(self):
        self.click_element(self.PRIVACY_POLICY_CHECKBOX)

    def submit_registration(self):
        self.click_element(self.CONTINUE_BUTTON)

    def confirm_message(self):
        return self.get_element_text (self.CONFIRM_MESSAGE_TXT)




