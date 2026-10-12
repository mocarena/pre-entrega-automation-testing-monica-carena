
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.datos import leer_json_productos
from utils.saucedemo_helpers import login


PRODUCTOS = leer_json_productos()


@pytest.fixture
def usuario_logueado(driver):
    """Realiza login antes de probar el carrito."""
    login(driver)
    assert "/inventory.html" in driver.current_url
    return driver


@pytest.mark.parametrize(
    "producto",
    PRODUCTOS,
    ids=[producto["nombre"] for producto in PRODUCTOS]
)
def test_agregar_producto_desde_json(usuario_logueado, producto):
    """Agrega cada producto del JSON y verifica el carrito."""

    driver = usuario_logueado

    # Agrega el producto indicado en el JSON
    boton_agregar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, producto["xpath_add_button"])
    )
)
    boton_agregar.click()

    # Verifica que el carrito tenga un producto
    badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
        )
    )
    assert badge.text == "1"

    # Abre el carrito
    driver.find_element(
        By.CSS_SELECTOR,
        "[data-test='shopping-cart-link']"
    ).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/cart.html")
    )

    # Comprueba que el producto correcto esté en el carrito
    producto_carrito = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
        )
    )

    assert producto_carrito.text == producto["nombre"], (
        f"Esperaba '{producto['nombre']}', "
        f"pero encontré '{producto_carrito.text}'"
    )


@pytest.mark.smoke
def test_carrito_smoke(usuario_logueado):
    """Verifica la funcionalidad básica del carrito."""

    driver = usuario_logueado

    driver.find_element(
        By.XPATH,
        "//button[@data-test='add-to-cart-sauce-labs-backpack']"
    ).click()

    badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
        )
    )

    assert badge.text == "1"
