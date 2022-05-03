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


class TestCase7(BasicTest):
    def test_main(self):
        self.driver.get(Config.main_page_url)
        main_page = MainPage(self.driver)
        main_page.open_elements_page()
        elements_page = ElementsPage(self.driver)
        elements_page.upload_and_download()
