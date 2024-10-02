import pytest
from selenium import webdriver

#@pytest.fixture(params=["chrome","edge"])
@pytest.fixture(autouse=True)
def setup_and_teardown(request):
    browser = request.config.getoption("--browser")
    global driver
    # if request.param == "chrome":
    #     driver = webdriver.Chrome()
    # elif request.param == "edge":
    #     driver = webdriver.Edge()
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.instagram.com/accounts/login/?hl=en")
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
