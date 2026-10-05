# Pre-Entrega Automation Testing - Monica Carena

## Propósito

Proyecto de automatización web desarrollado con Python, Pytest y Selenium WebDriver sobre SauceDemo.

El objetivo es validar un flujo básico de QA automatizado:

1. Login con credenciales válidas.
2. Redirección al inventario.
3. Verificación del catálogo.
4. Identificación del primer producto.
5. Agregado del producto al carrito.
6. Validación del badge del carrito.
7. Verificación del producto dentro del carrito.

## Tecnologías

- Python 3
- Selenium WebDriver 4
- Pytest
- pytest-html
- Git / GitHub
- Google Chrome

## Estructura

```text
pre-entrega-automation-testing-monica-carena/
├── tests/
│   ├── conftest.py
│   └── test_saucedemo.py
├── utils/
│   ├── driver_factory.py
│   └── saucedemo_helpers.py
├── datos/
├── reports/
├── requirements.txt
├── pytest.ini
└── README.md
```

## Instalación

Crear y activar un entorno virtual:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Ejecutar todos los tests:

```bash
pytest -v
```

Generar reporte HTML:

```bash
pytest -v --html=reports/reporte.html --self-contained-html
```

Ejecutar específicamente:

```bash
pytest tests/test_saucedemo.py -v
```

## Casos de prueba

### Login

Valida:

- Usuario `standard_user`
- Contraseña `secret_sauce`
- URL `/inventory.html`
- Título `Swag Labs`
- Texto `Products`

### Catálogo

Valida:

- Existencia de productos.
- Nombre del primer producto.
- Precio del primer producto.
- Presencia del menú.
- Presencia del selector de ordenamiento.

### Carrito

Valida:

- Agregado del primer producto.
- Badge del carrito igual a `1`.
- Navegación a `/cart.html`.
- Producto correcto dentro del carrito.

## Estrategias de localización

El proyecto utiliza las estrategias solicitadas durante las clases:

- `By.ID`
- `By.NAME`
- `By.CSS_SELECTOR`

Ejemplos:

```python
By.ID, "user-name"
By.NAME, "password"
By.CSS_SELECTOR, "#login-button"
```

Para el badge se utiliza una espera explícita:

```python
WebDriverWait(driver, 10)
```

Esto evita depender de esperas fijas y hace la automatización más robusta.

## Independencia de los tests

Cada test crea su propio WebDriver, realiza su propio login y cierra el navegador al finalizar. Por lo tanto, una falla no debería afectar el estado de los demás tests.

## Evidencias

En caso de fallo, `conftest.py` genera automáticamente una captura PNG dentro de `reports/`.

El reporte HTML también permite revisar el resultado de la ejecución.

## GitHub

Repositorio sugerido:

`pre-entrega-automation-testing-monica-carena`

Ejemplo de commits:

```text
feat: add SauceDemo login automation
test: validate inventory catalog
test: add shopping cart validation
feat: add failure screenshots
docs: add project README
chore: configure pytest html report
```
