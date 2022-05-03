from Pages.Main_Page import MainPage
from WebDriver import WebDriver
import Config
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


class TestCase5(BasicTest):
    def test_main(self):
        self.driver.get(Config.main_page_url)
        main_page = MainPage(self.driver)
        main_page.open_widgets_page()
