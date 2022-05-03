from selenium.webdriver.common.by import By
from Pages.Base_Page import AbstractBasePage
from Elements.Button import Button
from Elements.Text import Text
from WebDriver.Driver_Utils import AlertUtils


class AlertsPage(AbstractBasePage):
    """TestCase1"""
    alerts_page_unique_elem = (By.XPATH, '//*[@id="app"]//div[@class="main-header"]')

    left_alerts_button = (By.XPATH, '(//*[@id="item-1"])[2]')
    alerts_form = (By.XPATH, '//*[@id="javascriptAlertsWrapper"]')
    alerts_default_button = (By.XPATH, '//*[@id="alertButton"]')
    alerts_confirm_button = (By.XPATH, '//*[@id="confirmButton"]')
    alerts_prompt_button = (By.XPATH, '//*[@id="promtButton"]')
    alerts_prompt_user_text = (By.XPATH, '//*[@id="promptResult"]')

    """TestCase2"""
    nested_frames_button = (By.XPATH, '(//*[@id="item-3"])[2]')
    frames_button = (By.XPATH, '(//*[@id="item-2"])[2]')

    """TestCase4"""
    left_browser_window_button = (By.XPATH, '(//*[@id="item-0"])[3]')
    new_tab_button = (By.XPATH, '//*[@id="tabButton"]')

    def __init__(self, driver):
        locators = AlertsPage.alerts_page_unique_elem
        super().__init__(driver, locators)

    def default_alert(self):
        default_alert = Button(self.driver, AlertsPage.left_alerts_button)
        default_alert.default_click()

        default_alert_button = Button(self.driver, AlertsPage.alerts_default_button)
        default_alert_button.default_click()

        assert AlertUtils.check_alert(self.driver, 0)

    def confirm_button(self):
        confirm_button = Button(self.driver, AlertsPage.alerts_confirm_button)
        confirm_button.default_click()

        assert AlertUtils.check_alert(self.driver, 1)

    def prompt_button(self):
        prompt_button = Button(self.driver, AlertsPage.alerts_prompt_button)
        prompt_button.default_click()

        prompt_text_result_text = AlertUtils.check_alert(self.driver, 2)
        prompt_text_default_text = Text(self.driver, AlertsPage.alerts_prompt_user_text)

    def nested_frames(self):
        nested_frames = Button(self.driver, AlertsPage.nested_frames_button)
        nested_frames.default_click()

        frames = Button(self.driver, AlertsPage.frames_button)
        frames.default_click()

    def browser_windows(self):
        browser_windows_button = Button(self.driver, AlertsPage.left_browser_window_button)
        browser_windows_button.default_click()

        new_tab_button = Button(self.driver, AlertsPage.new_tab_button)
        new_tab_button.default_click()
