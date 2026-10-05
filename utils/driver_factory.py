from selenium import webdriver

def create_driver():
    """Create and return a Chrome WebDriver instance."""
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Optional for CI environments.
    return webdriver.Chrome(options=options)
