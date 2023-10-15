import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="input language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    chrome_options = Options()
    chrome_options.add_argument(f"--lang={language}")
    browser = webdriver.Chrome(chrome_options)
    yield browser
    print("\nquit browser..")
    browser.quit()
