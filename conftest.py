import pytest

from utilities.driver_factory import get_driver
from utilities.config_reader import ConfigReader
from utilities.locator_reader import LocatorReader
from utilities.screenshot import capture


ConfigReader.load_config()
LocatorReader.load_locators()


@pytest.fixture
def driver():

    driver = get_driver()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["driver"]

        capture(driver, item.name)
