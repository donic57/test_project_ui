from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


def test_add_cart(driver):
    driver.get('https://magento.softwaretestingboard.com/collections/eco-friendly.html')
    choice_bella_tank = driver.find_element(By.CSS_SELECTOR, '[alt="Bella Tank"]')
    text_one_page = driver.find_element(
        By.LINK_TEXT, 'Bella Tank').text
    actions = ActionChains(driver)
    actions.move_to_element(choice_bella_tank).click().perform()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[id="option-label-size-143-item-167"]')))
    size = driver.find_element(By.CSS_SELECTOR, '[id="option-label-size-143-item-167"]')
    color = driver.find_element(By.ID, 'option-label-color-93-item-50')
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[id="option-label-size-143-item-167"]')))
    size.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'option-label-color-93-item-50')))
    color.click()
    button_add_to_cart = driver.find_element(By.CSS_SELECTOR, '[title="Add to Cart"]')
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="Add to Cart"]')))
    actions.move_to_element(button_add_to_cart).click().perform()
    text_two_page = driver.find_element(By.CSS_SELECTOR, '[class="base"]').text
    size_text = driver.find_element(By.XPATH, '//span[normalize-space()="S"]').text
    color_text = driver.find_element(By.XPATH, '//span[normalize-space()="Blue"]').text
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')))
    text_add_cart = driver.find_element(
        By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]').text
    counter_number = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[class="counter-number"]'))).text
    assert text_one_page == text_two_page
    assert size_text == 'S'
    assert color_text == 'Blue'
    assert text_add_cart == 'You added Bella Tank to your shopping cart.'
    assert counter_number == '1'


def test_add_compare(driver):
    driver.get('https://magento.softwaretestingboard.com/collections/eco-friendly.html')
    choice_bella_tank = driver.find_element(By.XPATH, '//img[@alt="Bella Tank"]')
    actions = ActionChains(driver)
    actions.move_to_element(choice_bella_tank).perform()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '(//a[@title="Add to Compare"])[4]')))
    button_add_to_compare = driver.find_element(By.XPATH, '(//a[@title="Add to Compare"])[4]')
    actions.move_to_element(button_add_to_compare).click(button_add_to_compare).perform()
    text_one = driver.find_element(
        By.LINK_TEXT, 'Bella Tank').text
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '#compare-items > li > strong > a')))
    text_two = driver.find_element(
        By.CSS_SELECTOR, '#compare-items > li > strong > a').get_attribute('innerText')
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')))
    text_add_product = driver.find_element(
        By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]').text
    assert text_one == text_two
    assert text_add_product == 'You added product Bella Tank to the comparison list.'


def test_add_wish_list(driver):
    email = 'tesstqa@mail.ru'
    password = '12345aa!'
    driver.get('https://magento.softwaretestingboard.com/collections/eco-friendly.html')
    choice_bella_tank = driver.find_element(By.XPATH, '//img[@alt="Bella Tank"]')
    text_one_page = driver.find_element(
        By.LINK_TEXT, 'Bella Tank').text
    actions = ActionChains(driver)
    actions.move_to_element(choice_bella_tank).perform()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '(//a[@title="Add to Wish List"])[4]')))
    button_add_wish_list = driver.find_element(
        By.XPATH, '(//a[@title="Add to Wish List"])[4]')
    actions.move_to_element(button_add_wish_list).click(button_add_wish_list).perform()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[name="login[username]"]')))
    text_page_login = driver.find_element(
        By.XPATH, '//span[normalize-space()="Customer Login"]').text
    assert text_page_login == 'Customer Login'
    add_enail = driver.find_element(By.CSS_SELECTOR, '[name="login[username]"]')
    add_password = driver.find_element(By.CSS_SELECTOR, '[name="login[password]"]')
    add_enail.send_keys(email)
    add_password.send_keys(password)
    button_sign_in = driver.find_element(By.NAME, 'send')
    button_sign_in.click()
    driver.find_element(By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')))
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]'),
            'Bella Tank has been added to your Wish List. Click here to continue shopping.'))
    text_add_wish_list = driver.find_element(
        By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]').text
    text_pege_my_wish_list = driver.find_element(By.XPATH, '//span[normalize-space()="My Wish List"]').text
    text_two_page = driver.find_element(
        By.LINK_TEXT, 'Bella Tank').text
    assert text_add_wish_list == 'Bella Tank has been added to your Wish List. Click here to continue shopping.'
    assert text_pege_my_wish_list == 'My Wish List'
    assert text_one_page == text_two_page



