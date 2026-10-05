import pytest
from utils.driver_factory import create_driver
from utils.saucedemo_helpers import save_screenshot

@pytest.fixture
def driver(request):
    driver = create_driver()
    driver.maximize_window()
    yield driver
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        save_screenshot(driver, request.node.name)
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
