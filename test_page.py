import logging
import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By

class TestSearchLocators:
    ids = dict()
    with open('./locators.yaml', encoding='utf-8') as fy:
        locators = yaml.safe_load(fy)
        for locator in locators['xpath'].keys():
            ids[locator] = (By.XPATH, locators['xpath'][locator])
        for locator in locators['css'].keys():
            ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])


class OperationHelper(BasePage):
    def enter_text_into_field(self, locator, text, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'send work "{text}" in element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'element {locator} - not found')
            return False
        try:
            field.clear()
            field.send_keys(text)
        except:
            logging.exception(f'Exception while operation in locator {locator}')
            return False
        return True

    def enter_login(self, login):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], login, description='login form')