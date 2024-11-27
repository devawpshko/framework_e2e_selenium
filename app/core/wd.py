import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class WD:

    def __init__(self, *args, **kwargs):
        self.request = kwargs.get("request")
        self.webdriver_provider = kwargs.get("webdriver_provider")

        self.browser_name = kwargs.get("browser")
        self.browser_version = kwargs.get("browser_version")

        self.wd = self.get_driver()

    def get_driver(self):
        """
        Configure and return a WebDriver instance based on the specified browser.

        This method initializes a WebDriver for the browser specified by
        self.browser_name. Supports Chrome, Firefox, and Microsoft Edge.
        Custom configurations for download directories, pop-up handling,
        and PDF handling are set for each browser.

        If the webdriver_provider is "selenoid", additional configurations
        for Selenoid are applied, such as screen resolution and VNC support.
        The created WebDriver will have its window maximized before being
        returned.

        :return: WebDriver instance with the specified configurations
        :rtype: WebDriver
        """
        if self.browser_name == "chrome":
            options = ChromeOptions()
            prefs = {
                "profile.default_content_settings.popups": 0,  # Disable pop-ups
                "download.default_directory": "/home/selenium/Downloads",  # Set default download directory
                "profile.default_content_setting_values.notifications": 2,  # Disable notifications
                "plugins.always_open_pdf_externally": True,  # Download PDF files instead of automatically opening them
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
            }
            options.add_experimental_option("prefs", prefs)
        elif self.browser_name == "firefox":
            options = FirefoxOptions()
            options.set_preference("browser.download.dir", "/home/selenium/Downloads")
            options.set_preference("browser.download.folderList", 2)
            options.set_preference("browser.download.useDownloadDir", True)
            options.set_preference("pdfjs.disabled", True)
        elif self.browser_name == "MicrosoftEdge":
            options = EdgeOptions()
            prefs = {
                "profile.default_content_settings.popups": 0,  # Disable pop-ups
                "download.default_directory": "/home/selenium/Downloads",  # Set default download directory
                "profile.default_content_setting_values.notifications": 2,  # Disable notifications
                "plugins.always_open_pdf_externally": True,  # Download PDF files instead of automatically opening them
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
            }
            options.add_experimental_option("prefs", prefs)
        else:
            options = None

        options.headless = False
        options.browser_version = self.browser_version

        if self.webdriver_provider == "selenoid":
            selenoid_options = {
                "screenResolution": "1920x1080x24",
                "enableVNC": True,
                "enableVideo": False,
                "name": self.request.node.name
            }
            options.set_capability('selenoid:options', selenoid_options)
            selenium_endpoint = f"{os.environ.get("SELENOID_URL")}/wd/hub"
        else:
            selenium_endpoint = None
        driver = webdriver.Remote(command_executor=selenium_endpoint, options=options)
        driver.maximize_window()
        return driver

    def wd_kill(self):
        self.wd.quit()
