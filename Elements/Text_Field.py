from Elements.Base_Elements import AbstractBaceElements


class TextField(AbstractBaceElements):
    def default_send_keys(self, text):
        self.element.send_keys(text)
