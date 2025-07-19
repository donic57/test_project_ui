from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(5)
    chrome_driver.maximize_window()
    return chrome_driver




