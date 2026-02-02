from Pages import login_Page
from utils.driver_factory import get_driver
from selenium.webdriver.support import expected_conditions as EC

# Positive Test Cases
def test_login_success():
    driver = get_driver()
    login_Page.open_login_page(driver)
    login_Page.login(driver, "standard_user", "secret_sauce")

    assert login_Page.is_products_page_loaded(driver)
    assert login_Page.get_page_title(driver).text == "Products"

    driver.quit()


# Negative Test Cases
def test_login_invalid_password():
    driver = get_driver()
    login_Page.open_login_page(driver)
    login_Page.login(driver, "standard_user", "wrong_password")
    
    assert "Epic sadface: Username and password do not match any user in this service" in login_Page.get_error_message(driver)
    driver.quit()

def test_login_invalid_username():
    driver = get_driver()
    login_Page.open_login_page(driver)
    login_Page.login(driver, "wrong_user", "secret_sauce")
    
    assert "Epic sadface: Username and password do not match any user in this service" in login_Page.get_error_message(driver)
    driver.quit()

def test_login_empty_username_and_password():
    driver = get_driver()
    login_Page.open_login_page(driver)
    login_Page.login(driver, "", "")
    
    assert "Epic sadface: Username is required" in login_Page.get_error_message(driver)
    driver.quit()

def test_navigate_to_products_without_login():
    driver = get_driver()

    driver.get("https://www.saucedemo.com/inventory.html")

    assert "saucedemo.com" in driver.current_url
    assert "inventory" not in driver.current_url
    assert "Epic sadface: You can only access '/inventory.html' when you are logged in." in login_Page.get_error_message(driver)
    driver.quit()

def test_navigate_to_cart_without_login():
    driver = get_driver()

    driver.get("https://www.saucedemo.com/cart.html")

    assert "saucedemo.com" in driver.current_url
    assert "cart" not in driver.current_url
    assert "Epic sadface: You can only access '/cart.html' when you are logged in." in login_Page.get_error_message(driver)
    driver.quit()
