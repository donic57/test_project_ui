from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


def test_new_account_bad_registration(driver):
    driver.get('https://magento.softwaretestingboard.com/customer/account/create/')
    fild_first_name = driver.find_element(By.ID, 'firstname')
    fild_last_name = driver.find_element(By.ID, 'lastname')
    password = driver.find_element(By.ID, 'password')
    confirm_password = driver.find_element(By.ID, 'password-confirmation')
    button = driver.find_element(By.CSS_SELECTOR, '[class="action submit primary"]')
    fild_first_name.send_keys('test')
    fild_last_name.send_keys('test')
    password.send_keys('53535fsdfsdf')
    confirm_password.send_keys('53535fsdfsdf')
    button.click()
    password_error = driver.find_element(By.ID, 'password-error')
    email_address_error = driver.find_element(By.ID, 'email_address-error')
    assert password_error.text == ('Minimum of different classes of characters '
                                   'in password is 3. Classes of characters: '
                                   'Lower Case, Upper Case, Digits, Special Characters.')
    assert email_address_error.text == 'This is a required field.'


def test_new_account_success(driver):
    faker = Faker()
    driver.get('https://magento.softwaretestingboard.com/customer/account/create/')
    fild_first_name = driver.find_element(By.ID, 'firstname')
    fild_last_name = driver.find_element(By.ID, 'lastname')
    email_address = driver.find_element(By.ID, 'email_address')
    password = driver.find_element(By.ID, 'password')
    confirm_password = driver.find_element(By.ID, 'password-confirmation')
    button = driver.find_element(By.CSS_SELECTOR, '[class="action submit primary"]')
    fild_first_name.send_keys('test')
    fild_last_name.send_keys('test')
    email_address.send_keys(faker.email())
    password.send_keys('!53535fsdfsdf')
    confirm_password.send_keys('!53535fsdfsdf')
    button.click()
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')))
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]'),
            'Thank you for registering with Main Website Store.'))
    assert success_message.text == 'Thank you for registering with Main Website Store.'


def test_check_text(driver):
    driver.get('https://magento.softwaretestingboard.com/customer/account/create/')
    text_website = driver.find_element(By.ID, 'maincontent')
    assert text_website.get_attribute('innerText') == ('Create New Customer Account\nPersonal'
                            ' Information\nFirst Name\nLast Name\nSign-in'
                            ' Information\nEmail\nPassword\nPassword Strength:'
                            ' No Password\nConfirm Password\nCreate an Account')