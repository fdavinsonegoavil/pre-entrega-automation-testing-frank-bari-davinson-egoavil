import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage           
from pages.check_page import CheckPage         
import time 

def test_add_items_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckPage(driver)


    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    time.sleep(0.5)
    inventory_page.is_loaded()
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()
    inventory_page.add_bolt_t_shirt_to_cart()
    inventory_page.go_to_cart()
    time.sleep(0.5)
    cart_page.is_loaded()
    cart_page.click_checkout()
    time.sleep(0.5)
    checkout_page.is_loaded()
    checkout_page.completar_informacion_checkout("Jorge", "Ruiz", "12345")
    time.sleep(0.5)
    checkout_page.click_finish()
    time.sleep(0.5)
    checkout_page.back_to_home()

    