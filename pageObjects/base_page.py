import os

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    # ------------Constructore----------

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait=WebDriverWait(self.driver,20)

    # --- Regular Click (The Industry Standard) ---
    def click_element(self,locator):
        # The '*' here handles the unpacking for the whole framework!
        element=self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    #- JS -script Click in case faced and click failures as Backup
    def js_click(self, locator):
        element=self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();",element)
        pass

    #-SendKeys() -
    def type_text(self,locator,text):
        element=self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    #- JS -script Click in case faced and click failures as Backup
    def js_type_text(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        # This injects the value directly into the HTML element
        self.driver.execute_script("arguments[0].value = arguments[1];", element, text)

    #- Get Attribute("value")
    def get_attribute_value(self, locatore):
        element=self.wait.until(EC.presence_of_element_located(locatore))
        return element.get_attribute("value")

    # --- JS Backup for Value (The "Nerd" version) ---
    def js_get_attribute_value(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.execute_script("return arguments[0].value;", element)

    #-FindElements (FetchMultipleElemensts)
    def get_multiple_elements(self,locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    # --- Get Text with Visibility ---
    def get_element_text(self, locator):
        # We wait until the element is actually VISIBLE to a human
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    # JS Get Value (Fixes Stale/Hidden text issues)
    def js_get_text(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.execute_script("return arguments[0].innerText;", element)

