
import pytest

from utils.datos import leer_csv_login
from utils.saucedemo_helpers import login


CASOS_LOGIN = leer_csv_login()


@pytest.mark.parametrize(
    "usuario, clave, debe_funcionar, descripcion",
    CASOS_LOGIN,
    ids=[caso[3] for caso in CASOS_LOGIN]
)
def test_login_desde_csv(
    driver, usuario, clave, debe_funcionar, descripcion
):
    """Valida distintos escenarios de login con datos externos."""

    resultado = login(driver, usuario, clave)

    if debe_funcionar:
        assert resultado is True, (
            f"Se esperaba un login exitoso: {descripcion}"
        )
        assert "/inventory.html" in driver.current_url
    else:
        assert resultado is False, (
            f"Se esperaba un login fallido: {descripcion}"
        )


@pytest.mark.smoke
def test_login_usuario_valido_smoke(driver):
    """Comprueba el acceso básico con un usuario válido."""

    resultado = login(driver)

    assert resultado is True
    assert "/inventory.html" in driver.current_url