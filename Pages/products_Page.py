from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Locators
ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
PRODUCTS_TITLE = (By.CLASS_NAME, "title")

# Page actions
def is_products_page_open(driver):
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(PRODUCTS_TITLE)
    )


def add_backpack_to_cart(driver):
    driver.find_element(*ADD_TO_CART_BACKPACK).click()


def remove_backpack_from_cart(driver):
    driver.find_element(*REMOVE_BACKPACK).click()


def get_cart_count(driver):
    return driver.find_element(*CART_BADGE).text


def is_cart_badge_displayed(driver):
    return len(driver.find_elements(*CART_BADGE)) > 0
