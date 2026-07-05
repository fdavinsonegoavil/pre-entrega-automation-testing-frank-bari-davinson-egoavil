from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_successful_login(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    login_page.click()

    assert inventory_page.is_loaded(), "El inventario no se cargó; el login falló."