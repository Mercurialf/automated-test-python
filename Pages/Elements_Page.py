from selenium.webdriver.common.by import By
from Elements.Button import Button
from Elements.Text_Field import TextField
from Pages.Base_Page import AbstractBasePage


class ElementsPage(AbstractBasePage):
    elements_page_unique_elem = (By.XPATH, '//*[@id="app"]//div[@class="main-header"]')
    left_elements_button = (By.XPATH, '(//*[@id="item-3"])[1]')
    add_button = (By.XPATH, '//*[@id="addNewRecordButton"]')
    first_name = (By.XPATH, '//*[@id="firstName"]')
    last_name = (By.XPATH, '//*[@id="lastName"]')
    user_email = (By.XPATH, '//*[@id="userEmail"]')
    user_age = (By.XPATH, '//*[@id="age"]')
    user_salary = (By.XPATH, '//*[@id="salary"]')
    user_department = (By.XPATH, '//*[@id="department"]')
    submit_button = (By.XPATH, '//*[@id="submit"]')
    delete_button = (By.XPATH, '//*[@id="delete-record-4"]')

    """TestCase7"""
    left_upload_and_download = (By.XPATH, '(//*[@id="item-7"]/span)[1]')
    download = (By.XPATH, '//*[@id="downloadButton"]')
    choose_file = (By.XPATH, '//*[@id="uploadFile"]')

    def __init__(self, driver):
        locators = ElementsPage.elements_page_unique_elem
        super().__init__(driver, locators)

    def open_web_tables(self):
        element_button = Button(self.driver, ElementsPage.left_elements_button)
        element_button.default_click()

    def input_web_tables(self, user):
        element_add_button = Button(self.driver, ElementsPage.add_button)
        element_add_button.default_click()

        first_name = TextField(self.driver, ElementsPage.first_name)
        first_name.default_send_keys(user[0])
        last_name = TextField(self.driver, ElementsPage.last_name)
        last_name.default_send_keys(user[1])

        user_email = TextField(self.driver, ElementsPage.user_email)
        user_email.default_send_keys(user[2])
        user_age = TextField(self.driver, ElementsPage.user_age)
        user_age.default_send_keys(user[3])

        user_salary = TextField(self.driver, ElementsPage.user_salary)
        user_salary.default_send_keys(user[4])
        user_department = TextField(self.driver, ElementsPage.user_department)
        user_department.default_send_keys(user[5])

        submit_button = Button(self.driver, ElementsPage.submit_button)
        submit_button.default_click()

    def delete_user(self):
        delete_button = Button(self.driver, ElementsPage.delete_button)
        delete_button.default_click()

    def upload_and_download(self):
        left_upload_and_download = Button(self.driver, ElementsPage.left_upload_and_download)
        left_upload_and_download.default_click()
        download_button = Button(self.driver, ElementsPage.download)
        download_button.default_click()
