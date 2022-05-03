from selenium.webdriver.common.by import By
from Pages.Base_Page import AbstractBasePage
from Elements.Button import Button
from Elements.Text_Field import TextField


class WidgetsPage(AbstractBasePage):
    widgets_page_unique_elem = (By.XPATH, '//*[@id="app"]//div[@class="main-header"]')
    """TestCase6"""
    data_picker_left_button = (By.XPATH, '(//*[@id="item-2"]/span)[3]')
    select_date = (By.XPATH, '//*[@id="datePickerMonthYearInput"]')
    year_select_menu = (By.XPATH, '(//*[@id="datePickerMonthYear"]//select)[2]')
    year_select = (By.XPATH, '//*[@id="datePickerMonthYear"]//select/option[125]')
    month_select_menu = (By.XPATH, '(//*[@id="datePickerMonthYear"]//select)[1]')
    month_select = (By.XPATH, '(//*[@id="datePickerMonthYear"]//select/option[2])[1]')
    day_select = (By.XPATH, '//div[@aria-label="Choose Thursday, February 29th, 2024"]')
    """TestCase5"""
    left_slider_button = (By.XPATH, '(//*[@id="item-3"]/span)[3]')
    slider_value = (By.XPATH, '//*[@id="sliderValue"]')

    def __init__(self, driver):
        super().__init__(driver, WidgetsPage.widgets_page_unique_elem)

    def main_widgets_button(self):
        left_widgets_button = Button(self.driver, WidgetsPage.data_picker_left_button)
        left_widgets_button.default_click()

    def data_select(self):
        select_date = TextField(self.driver, WidgetsPage.select_date)
        select_date.default_click()

        year_menu = Button(self.driver, WidgetsPage.year_select_menu)
        year_menu.default_click()
        year_select = Button(self.driver, WidgetsPage.year_select)
        year_select.default_click()

        mouth_menu = Button(self.driver, WidgetsPage.month_select_menu)
        mouth_menu.default_click()
        mouth_select = Button(self.driver, WidgetsPage.month_select)
        mouth_select.default_click()

        day_select = Button(self.driver, WidgetsPage.day_select)
        day_select.default_click()
