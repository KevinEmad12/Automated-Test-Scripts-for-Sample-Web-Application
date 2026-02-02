from Pages import login_Page
from Pages import products_Page
from Pages import checkout_Page
from utils.driver_factory import get_driver

# Positive Flow
def test_successful_checkout():
    driver = get_driver()

    # Step 1: Login
    login_Page.open_login_page(driver)
    login_Page.login(driver, "standard_user", "secret_sauce")

    # Step 2: Add product
    products_Page.add_backpack_to_cart(driver)

    # Step 3: Checkout flow
    checkout_Page.go_to_cart(driver)
    checkout_Page.click_checkout(driver)
    checkout_Page.enter_checkout_info(driver, "John", "Doe", "12345")
    checkout_Page.finish_checkout(driver)

    assert checkout_Page.get_success_message(driver) == "Thank you for your order!"

    driver.quit()

def test_checkout_button_disabled_when_cart_empty():
    driver = get_driver()

    # Step 1: Login
    login_Page.open_login_page(driver)
    login_Page.login(driver, "standard_user", "secret_sauce")

    # Step 1: Open the cart
    checkout_Page.go_to_cart(driver)

    # Step 1: Checkout button should be disabled (No items in cart)
    checkout_button = driver.find_element(*checkout_Page.CHECKOUT_BUTTON)

    assert not checkout_button.is_enabled()

    driver.quit()

