from abc import ABC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config import base_waiting_time


class AbstractBaceElements(ABC):
    def __init__(self, driver, locators):
        self.driver = driver
        self.locators = locators
        self.element = WebDriverWait(driver, base_waiting_time).until(
            EC.presence_of_element_located((locators[0], locators[1])))
        assert self.element

    def default_click(self):
        self.element = WebDriverWait(self.driver, base_waiting_time).until(
            EC.element_to_be_clickable((self.locators[0], self.locators[1])))
        self.element.click()
