from selenium.webdriver.common.by import By

# Cart Locators
CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
CHECKOUT_BUTTON = (By.ID, "checkout")

# Checkout info Locators
FIRST_NAME = (By.ID, "first-name")
LAST_NAME = (By.ID, "last-name")
POSTAL_CODE = (By.ID, "postal-code")
CONTINUE_BUTTON = (By.ID, "continue")

# Finish Locators
FINISH_BUTTON = (By.ID, "finish")
SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

# Page actions
def go_to_cart(driver):
    driver.find_element(*CART_ICON).click()


def click_checkout(driver):
    driver.find_element(*CHECKOUT_BUTTON).click()


def enter_checkout_info(driver, first, last, postal):
    driver.find_element(*FIRST_NAME).send_keys(first)
    driver.find_element(*LAST_NAME).send_keys(last)
    driver.find_element(*POSTAL_CODE).send_keys(postal)
    driver.find_element(*CONTINUE_BUTTON).click()


def finish_checkout(driver):
    driver.find_element(*FINISH_BUTTON).click()


def get_success_message(driver):
    return driver.find_element(*SUCCESS_MESSAGE).text
