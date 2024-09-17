import pytest
from selenium import webdriver
from data import URL_QA_SCOOTER


@pytest.fixture(scope="function")
def driver():
    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(URL_QA_SCOOTER)
    driver.maximize_window()
    yield driver
    driver.quit()