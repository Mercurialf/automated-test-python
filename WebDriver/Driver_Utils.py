from Utils.Utils import *


class AlertUtils:
    alerts_list = ("You clicked a button", "Do you confirm action?", "Please enter your name")

    def __init__(self, driver):
        self.driver = driver
        self.page = self.driver.window_handles[0]

    def switch(self):
        self.driver.switch_to_window(self.page)

    @staticmethod
    def check_alert(driver, num):
        """Функция подтверждения и проверки сообщений 'Alert'."""
        alert = driver.switch_to.alert

        if num == 0:
            assert AlertUtils.alerts_list[0] in alert.text
            alert.accept()
            return True
        if num == 1:
            assert AlertUtils.alerts_list[1] in alert.text
            alert.accept()
            return True
        if num == 2:
            assert AlertUtils.alerts_list[2] in alert.text
            text = Utils.generate_random_string()
            alert.send_keys(text)
            alert.accept()
            return text
