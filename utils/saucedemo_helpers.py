from pathlib import Path
from datetime import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def login(driver, usuario=None, clave=None):
    """Log in to SauceDemo with the provided or default credentials."""
    wait = WebDriverWait(driver, 10)

    usuario = usuario or USERNAME
    clave = clave or PASSWORD

    driver.get(BASE_URL)

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys(usuario)

    driver.find_element(By.ID, "password").send_keys(clave)
    driver.find_element(By.ID, "login-button").click()

    try:
        wait.until(
            lambda d: "/inventory.html" in d.current_url
            or len(d.find_elements(By.CSS_SELECTOR, "[data-test='error']")) > 0
        )
    except TimeoutException:
        save_screenshot(driver, "login_failed")
        raise

    if "/inventory.html" in driver.current_url:
        return True

    return False

def save_screenshot(driver, test_name):
    """Save a screenshot for a failed test."""
    reports = Path("reports")
    reports.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = reports / f"{test_name}_{timestamp}.png"
    driver.save_screenshot(str(path))
    return path
