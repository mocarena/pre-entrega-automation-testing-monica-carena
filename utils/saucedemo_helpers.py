from pathlib import Path
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def login(driver):
    """Log in with valid SauceDemo credentials."""
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    wait.until(EC.url_contains("/inventory.html"))

def save_screenshot(driver, test_name):
    """Save a screenshot for a failed test."""
    reports = Path("reports")
    reports.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = reports / f"{test_name}_{timestamp}.png"
    driver.save_screenshot(str(path))
    return path
