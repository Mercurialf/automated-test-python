import Config
from WebDriver import WebDriver
from Pages.Main_Page import MainPage
from Pages.Elements_Page import ElementsPage
import pytest


@pytest.fixture(scope="class")
def driver_init(request):
    driver = WebDriver.IWebDriver().driver
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class TestCase3(BasicTest):
    def test_main_page(self):
        self.driver.get(Config.main_page_url)
        main_page = MainPage(self.driver)
        main_page.open_elements_page()
        elements_page = ElementsPage(self.driver)
        elements_page.open_web_tables()
        elements_page.input_web_tables(Config.user_account_1)
        elements_page.input_web_tables(Config.user_account_2)
        elements_page.delete_user()
