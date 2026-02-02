from Pages import products_Page
from Pages import login_Page
from utils.driver_factory import get_driver

def test_products_page_opens_after_login():
    driver = get_driver()
    login_Page.open_login_page(driver)
    login_Page.login(driver, "standard_user", "secret_sauce")

    assert products_Page.is_products_page_open(driver).text == "Products"

    driver.quit()

def test_add_item_to_cart():
    driver = get_driver()
    login_Page.open_login_page(driver)
    login_Page.login(driver, "standard_user", "secret_sauce")

    products_Page.add_backpack_to_cart(driver)

    assert products_Page.get_cart_count(driver) == "1"

    driver.quit()

def test_remove_item_from_cart():
    driver = get_driver()
    login_Page.open_login_page(driver)
    login_Page.login(driver, "standard_user", "secret_sauce")

    products_Page.add_backpack_to_cart(driver)
    products_Page.remove_backpack_from_cart(driver)

    assert not products_Page.is_cart_badge_displayed(driver)

    driver.quit()
