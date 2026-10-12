# Pre-Entrega Automation Testing - Monica Carena

## Propósito

Proyecto de automatización web desarrollado con Python, Pytest y Selenium WebDriver sobre [SauceDemo](https://www.saucedemo.com/).

El objetivo es validar funcionalidades principales de una aplicación web mediante pruebas automatizadas, aplicando buenas prácticas de QA, reutilización de código, parametrización y pruebas basadas en datos externos.

## Tecnologías

- Python 3
- Selenium WebDriver 4
- Pytest
- pytest-html
- Google Chrome
- Git / GitHub
- CSV y JSON para datos de prueba

## Estructura del proyecto

```text
pre-entrega-automation-testing-monica-carena/
├── tests/
│   ├── conftest.py
│   ├── test_saucedemo.py
│   ├── test_login_csv.py
│   └── test_carrito_json.py
├── utils/
│   ├── __init__.py
│   ├── driver_factory.py
│   ├── saucedemo_helpers.py
│   └── datos.py
├── datos/
│   ├── login.csv
│   └── productos.json
├── reports/
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

*Nota: la estructura debe coincidir con los archivos reales del repositorio.*

## Instalación

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
cd pre-entrega-automation-testing-monica-carena
```

Reemplazar `URL_DEL_REPOSITORIO` por la URL real del repositorio de GitHub.

### 2. Crear y activar un entorno virtual

```bash
python -m venv .venv
```

En Windows:

```powershell
.venv\Scripts\activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

Es necesario tener Google Chrome instalado y contar con una configuración compatible de Selenium WebDriver.

## Ejecución de las pruebas

Ejecutar toda la suite:

```bash
python -m pytest -v
```

Ejecutar los tests de login con datos CSV:

```bash
python -m pytest tests/test_login_csv.py -v
```

Ejecutar los tests del carrito con datos JSON:

```bash
python -m pytest tests/test_carrito_json.py -v
```

Ejecutar los tests generales de SauceDemo:

```bash
python -m pytest tests/test_saucedemo.py -v
```

Ejecutar las pruebas marcadas como smoke:

```bash
python -m pytest -m smoke -v
```

## Generación del reporte HTML

Para generar un reporte autocontenido con los resultados de la ejecución:

```bash
python -m pytest -v --html=reports/reporte.html --self-contained-html
```

Luego, abrir `reports/reporte.html` en el navegador para consultar los resultados.

## Casos de prueba implementados

### 1. Login y navegación

Se validan:

- Inicio de sesión con credenciales válidas.
- Redirección al inventario.
- Título de la página.
- Visualización del catálogo.
- Comportamiento ante credenciales inválidas y usuarios con restricciones.

### 2. Pruebas de login basadas en CSV

Los escenarios de autenticación se cargan desde `datos/login.csv`.

Se utiliza parametrización de Pytest para ejecutar múltiples casos con diferentes usuarios, contraseñas, resultados esperados y descripciones.

Esto facilita agregar nuevos escenarios sin duplicar la estructura del test.

### 3. Catálogo de productos

Se validan:

- Existencia de productos.
- Nombre y precio del primer producto.
- Presencia del menú.
- Presencia del selector de ordenamiento.

### 4. Carrito con datos desde JSON

Los productos se cargan desde `datos/productos.json`.

Se valida:

- Selección del botón correspondiente a cada producto.
- Incorporación del producto al carrito.
- Actualización del badge.
- Navegación a la página del carrito.
- Correspondencia entre el producto seleccionado y el producto agregado.

Los casos se parametrizan para reutilizar el mismo test con distintos productos.

### 5. Pruebas smoke

Se incluyen pruebas básicas para verificar rápidamente funcionalidades esenciales, como el login y el agregado de productos al carrito.

## Estrategias de localización y sincronización

El proyecto utiliza distintos localizadores de Selenium:

- `By.ID`
- `By.NAME`
- `By.CSS_SELECTOR`
- `By.XPATH`

Se emplean esperas explícitas con `WebDriverWait` y condiciones esperadas para sincronizar las acciones con el estado de la interfaz, evitando depender exclusivamente de esperas fijas.

## Reutilización y aislamiento

Las funciones auxiliares centralizan acciones comunes, como el inicio de sesión.

Los fixtures de Pytest administran la preparación y limpieza del navegador, favoreciendo la independencia entre los tests.

Los datos de prueba se mantienen separados del código para facilitar su mantenimiento y ampliación.

## Evidencias

El proyecto permite generar:

- Reportes HTML de ejecución.
- Capturas PNG ante fallos, según la configuración de `conftest.py`.
- Resultados individuales y parametrizados en la terminal.

## Objetivos de aprendizaje

Este proyecto integra prácticas de automatización orientadas a:

- Diseño y ejecución de pruebas funcionales.
- Uso de Selenium WebDriver.
- Parametrización con Pytest.
- Gestión externa de datos con CSV y JSON.
- Sincronización mediante esperas explícitas.
- Reutilización de funciones y fixtures.
- Generación de reportes y evidencias.
- Control de versiones con Git y GitHub.

## Repositorio

**Proyecto:** Pre-Entrega Automation Testing - Monica Carena

Repositorio: https://github.com/mocarena/pre-entrega-automation-testing-monica-carena/tree/main

