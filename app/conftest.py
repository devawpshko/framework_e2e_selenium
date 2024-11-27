import os

import pytest
from dotenv import load_dotenv

from core.application import Application
from core.wd import WD

BASE_PATH = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
ENV_FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, ".env"))


@pytest.fixture(scope="function")
def app(request):
    """
    Fixture to create and yield an Application instance configured for testing.

    If an environment file exists at `ENV_FILE_PATH`, this fixture
    loads it. The fixture retrieves the test environment and worker
    id, initializes a driver, and creates an Application instance.
    After yielding the application, it ensures the driver is properly
    terminated.

    :param request: pytest request object used to access test parameters.
    :type request: _pytest.fixtures.FixtureRequest
    :return: An instance of the Application configured for the test environment.
    :rtype: Application
    """
    if os.path.exists(ENV_FILE_PATH):
        load_dotenv(ENV_FILE_PATH)
    test_env = request.config.getoption("--test-env")
    worker_id = get_worker_id()
    driver = get_driver(request, worker_id)
    application = Application(
        worker_id=worker_id,
        test_env=test_env,
        driver=driver.wd
    )
    yield application
    request.addfinalizer(driver.wd_kill())


def get_worker_id():
    """
    Retrieves the worker ID from environment variables, particularly useful in
    parallel testing scenarios with pytest-xdist. If the worker ID is not set,
    it defaults to "gw0".
    """
    worker = os.environ.get('PYTEST_XDIST_WORKER')
    if worker is None:
        worker = "gw0"
    return int(worker.replace("gw", ""))


def get_driver(request, worker_id):
    """
    Get a WebDriver instance initialized with the specified options.

    The function retrieves the WebDriver provider, browser name, and browser version from
    the pytest request configuration options. It then returns an instance of the WD class
    initialized with these parameters, along with the given worker_id and request.
    """
    webdriver_provider = request.config.getoption("--webdriver-provider", default="selenoid")
    browser_name = request.config.getoption("--browser-name", default="chrome")
    browser_version = request.config.getoption("--browser-version", default="130.0")
    return WD(
        worker_id=worker_id,
        request=request,
        browser_name=browser_name,
        browser_version=browser_version,
        webdriver_provider=webdriver_provider
    )


def pytest_addoption(parser):
    """
    Adds custom command line options for pytest.

    This function registers additional command line options that can be used
    to specify the test environment, webdriver provider, browser name, and
    browser version when running pytest.
    """
    parser.addoption("--test-env", action="store", default=None,
                     help="Environment to run tests on")
    parser.addoption("--webdriver-provider", action="store", default=None,
                     help="Proxy or local webdriver provider.")
    parser.addoption("--browser-name", action="store", default=None,
                     help="Browser to run tests on")
    parser.addoption("--browser-version", action="store", default=None,
                     help="Browser version to run tests on")
