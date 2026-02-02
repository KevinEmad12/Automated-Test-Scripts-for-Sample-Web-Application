from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Locators
USERNAME_INPUT = (By.ID, "user-name")
PASSWORD_INPUT = (By.ID, "password")
LOGIN_BUTTON = (By.ID, "login-button")
ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
INVENTORY_CONTAINER = (By.ID,"inventory_container")
PAGE_TITLE = (By.CLASS_NAME,"title")

# Page actions
def open_login_page(driver):
    driver.get("https://www.saucedemo.com")


def login(driver, username, password):
    driver.find_element(*USERNAME_INPUT).send_keys(username)
    driver.find_element(*PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LOGIN_BUTTON).click()


def get_error_message(driver):
    return driver.find_element(*ERROR_MESSAGE).text


def is_products_page_loaded(driver):
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(INVENTORY_CONTAINER)
    )


def get_page_title(driver):
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(PAGE_TITLE)
    )