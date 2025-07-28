from selenium import webdriver
import pytest
from pages.customer_account import CustomerAccount
from pages.sale_page import SalePage
from pages.eco_friendly_page import EcoFriendlyPage


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(5)
    chrome_driver.maximize_window()
    return chrome_driver


@pytest.fixture()
def account_page(driver):
    return CustomerAccount(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def eco_friendly(driver):
    return EcoFriendlyPage(driver)
