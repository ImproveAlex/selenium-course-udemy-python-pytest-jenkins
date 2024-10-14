import pytest
import os
from selenium import webdriver
driver = None

download_folder = "C:\\Users\\Alex\\Documents\\Udemy-selenium-python\\PythonSelFramework\\testData"
desired_file_name = "fruits.xlsx"  # Change to your desired name
downloaded_extension = ".xlsx"

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default= "Chrome", help="Browser to run the tests")
    parser.addoption("--url", action="store", default="https://rahulshettyacademy.com/angularpractice/",
                     help="URL to test")

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    url = request.config.getoption("url")
    if browser_name == "Chrome":
        chrome_options = webdriver.ChromeOptions()
        prefs = {
            "download.default_directory": download_folder,  # Set download folder
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
        }
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "Firefox":
        driver = webdriver.Firefox()

    elif browser_name == "Edge":
            edge_options = webdriver.EdgeOptions()
            edge_options.add_experimental_option("prefs", {"download.default_directory": download_folder})
            driver = webdriver.Edge(options=edge_options)
    else:
        raise Exception(f"Browser {browser_name} is not supported")

    driver.implicitly_wait(5)
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

