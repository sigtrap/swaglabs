from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select as WebDriverSelect
import time


class ClientInfoPage(BasePage):

    _first_name =  {"by": By.XPATH, "value": "//input[@id='first-name']"}
    _last_name = {"by": By.XPATH, "value": "//input[@id='last-name']"}
    _zipcode = {"by": By.XPATH, "value": "//input[@id='postal-code']"}
    _continue = {"by": By.XPATH, "value": "//input[@class='btn_primary cart_button']"}
    #will go back to cart html
    _cancel = {"by": By.CLASS_NAME, "value": "cart_cancel_link btn_secondary"}
    _warning = {"by": By.XPATH, "value": "//h3[1]"}

    def input_first_name(self, first_name):
        try:
            self._is_displayed(self._first_name)
            self._clear(self._first_name)
            self._send_keys(self._first_name, first_name)

        except NoSuchElementException:
            return False

    def input_last_name(self, last_name):
        try:
            self._is_displayed(self._last_name)
            self._clear(self._last_name)
            self._send_keys(self._last_name, last_name)

        except NoSuchElementException:
            return False


    def input_zipcode(self, zipcode):
        try:
            self._is_displayed(self._zipcode)
            self._clear(self._zipcode)
            self._send_keys(self._zipcode, zipcode)

        except NoSuchElementException:
            return False


    def continue_button(self):

        try:
            self._is_displayed(self._continue)
            return self._find(self._continue)

        except NoSuchElementException:
            return False

    #will go back to page of https://www.saucedemo.com/cart.html
    def cancel_button(self):

        try:
            self._is_displayed(self._cancel)
            self._click(self._cancel)

        except NoSuchElementException:
            return False


    def warning_sign(self):
        result = ""
        try:
            self._is_displayed(self._warning)

            result = self._find(self._warning)


        except NoSuchElementException:
            result = False


        finally:
            return result









