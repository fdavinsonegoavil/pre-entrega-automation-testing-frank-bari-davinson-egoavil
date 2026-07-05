import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage           
from pages.check_page import CheckPage          

def test_add_items_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckPage(driver)


    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()
    inventory_page.add_bolt_t_shirt_to_cart()
    inventory_page.go_to_cart()
    cart_page.click_checkout()
    checkout_page.completar_informacion_checkout("Jorge", "Ruiz", "12345")
    checkout_page.click_finish()
    checkout_page.back_to_home()

    