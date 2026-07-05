from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    BACK_TO_HOME_BUTTON = (By.ID, "back-to-products")

    def __init__(self, driver):
        super().__init__(driver)

    def is_loaded(self):
        return self.find_element(self.FIRST_NAME_INPUT).is_displayed()

    def completar_informacion_checkout(self, first_name, last_name, zip_code):
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.ZIP_CODE_INPUT, zip_code)
        self.click(self.CONTINUE_BUTTON)

    def click_finish(self):
        self.click(self.FINISH_BUTTON)
    
    def back_to_home(self):
        self.click(self.BACK_TO_HOME_BUTTON)