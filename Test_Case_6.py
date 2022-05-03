import Config
from WebDriver import WebDriver
from Pages.Main_Page import MainPage
from Pages.Widgets_Page import WidgetsPage
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


class TestCase6(BasicTest):
    def test_main(self):
        self.driver.get(Config.main_page_url)
        main_page = MainPage(self.driver)
        main_page.open_widgets_page()
        widgets_page = WidgetsPage(self.driver)
        widgets_page.main_widgets_button()
        widgets_page.data_select()
