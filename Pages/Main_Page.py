from selenium.webdriver.common.by import By
from Elements.Button import Button
from Pages.Base_Page import AbstractBasePage


class MainPage(AbstractBasePage):
    main_page_unique_elem = (By.XPATH, "//*[@id='app']//div[@class='home-banner']")
    alert_page_button = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[3]')
    elements_page_button = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]')
    widgets_page_button = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[4]')

    def __init__(self, driver):
        locators = MainPage.main_page_unique_elem
        super().__init__(driver, locators)

    def open_alert_page(self):
        alert_button = Button(self.driver, MainPage.alert_page_button)
        alert_button.default_click()

    def open_elements_page(self):
        elements_button = Button(self.driver, MainPage.elements_page_button)
        elements_button.default_click()

    def open_widgets_page(self):
        widgets_button = Button(self.driver, MainPage.widgets_page_button)
        widgets_button.default_click()
