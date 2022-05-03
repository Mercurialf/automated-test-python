import Config
from WebDriver import WebDriver
from Pages.Main_Page import MainPage
from Pages.Alerts_Page import AlertsPage
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


class TestCase4(BasicTest):
    def test_main_page(self):
        self.driver.get(Config.main_page_url)
        main_page = MainPage(self.driver)
        main_page.open_alert_page()
        alerts_page = AlertsPage(self.driver)
        alerts_page.browser_windows()
