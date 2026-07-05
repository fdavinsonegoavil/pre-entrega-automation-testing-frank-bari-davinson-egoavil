from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    # CORREGIMOS LOS LOCALIZADORES APUNTANDO A CSS_SELECTOR:
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    ADD_TO_CART_BUTTON_BACK_PACK = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    ADD_TO_CART_BUTTON_BIKE_LIGHT = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light")
    ADD_TO_CART_BUTTON_BOLT_T_SHIRT = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        super().__init__(driver)

    def is_loaded(self):
        return self.find_element(self.INVENTORY_CONTAINER).is_displayed()

    def add_backpack_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON_BACK_PACK)

    def add_bike_light_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON_BIKE_LIGHT)

    def add_bolt_t_shirt_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON_BOLT_T_SHIRT)

    def go_to_cart(self):
        self.click(self.SHOPPING_CART_LINK)