import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def base_url():
    return "https://www.lambdatest.com/selenium-playground/"

@pytest.fixture(scope="function")
def driver(request):
    options=webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    request.node.driver=driver
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome=yield
    report=outcome.get_result()
    if report.when=="call" and report.failed:
        drv=getattr(item,"driver",None)
        if drv:
            drv.save_screenshot(f"{item.name}_failure.png")
