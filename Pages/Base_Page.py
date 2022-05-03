from abc import ABC, abstractmethod
from Utils.LoggerUtils import Logging


class AbstractBasePage(ABC):
    @abstractmethod
    def __init__(self, driver, locators):
        self.driver = driver
        assert self.driver.find_element(locators[0], locators[1])
        Logging()
