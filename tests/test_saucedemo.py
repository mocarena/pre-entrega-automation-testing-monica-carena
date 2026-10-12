from selenium.webdriver.common.by import By
from utils.saucedemo_helpers import login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success(driver):
    """Validate successful login and inventory redirection."""
    login(driver)

    assert "/inventory.html" in driver.current_url
    assert driver.title == "Swag Labs"

    products_title = driver.find_element(
        By.CSS_SELECTOR, "div.header_secondary_container .title"
    )
    assert products_title.text == "Products"

def test_inventory_catalog(driver):
    """Validate inventory title, products, and first product data."""
    login(driver)

    assert driver.title == "Swag Labs"

    products = driver.find_elements(By.CSS_SELECTOR, "div.inventory_item")
    assert len(products) > 0, "No products were found in the inventory."

    first_product = products[0]
    name = first_product.find_element(
        By.CSS_SELECTOR, ".inventory_item_name"
    ).text
    price = first_product.find_element(
        By.CSS_SELECTOR, ".inventory_item_price"
    ).text

    print(f"First product: {name} | Price: {price}")

    assert name
    assert price.startswith("$")

    # Important interface elements: menu and sort/filter control.
    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, ".product_sort_container").is_displayed()

def test_add_product_to_cart(driver):
    """Add the first product and verify it is present in the cart."""
    login(driver)

    products = driver.find_elements(By.CSS_SELECTOR, "div.inventory_item")
    assert products, "No products available to add."

    first_product = products[0]
    product_name = first_product.find_element(
        By.CSS_SELECTOR, ".inventory_item_name"
    ).text

    first_product.find_element(
        By.CSS_SELECTOR, "button"
    ).click()

    wait = WebDriverWait(driver, 10)
    badge = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".shopping_cart_badge")
        )
    )
    assert badge.text == "1"

    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    wait.until(EC.url_contains("/cart.html"))

    cart_product = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
        )
    )
    assert cart_product.text == product_name

    print("Test OK")
