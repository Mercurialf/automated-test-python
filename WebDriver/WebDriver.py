from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


class IWebDriver:
    class __WebDriver:
        def __init__(self):
            # self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
            self.driver.maximize_window()

    driver = None

    def __init__(self):
        if not self.driver:
            IWebDriver.driver = IWebDriver.__WebDriver().driver
