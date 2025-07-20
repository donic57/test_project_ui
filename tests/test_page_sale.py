from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


def test_text_page_sale(driver):
    driver.get('https://magento.softwaretestingboard.com/sale.html')
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'base')))
    text_sale = driver.find_element(By.CLASS_NAME, 'base').text
    assert text_sale == 'Sale'
    text_categories_menu = driver.find_element(
        By.CLASS_NAME, 'categories-menu').get_attribute('innerText')
    assert text_categories_menu == ("Women's Deals\nHoodies and Sweatshirts\nJackets\n"
                                    "Tees\nBras & Tanks\nPants\nShorts\nMens's Deals\n"
                                    "Hoodies and Sweatshirts\nJackets\nTees\nPants\n"
                                    "Shorts\nGear Deals\nBags\nFitness Equipment")


def test_quantity_items_in_pages(driver):
    driver.get('https://magento.softwaretestingboard.com/sale.html')
    link_women_deals = driver.find_element(By.CSS_SELECTOR, '[class="more button"]')
    driver.execute_script('arguments[0].scrollIntoView();', link_women_deals)
    link_women_deals.click()
    text_page_women_sale = driver.find_element(
        By.XPATH, '//span[normalize-space()="Women Sale"]').text
    assert text_page_women_sale == 'Women Sale'
    quantity_items = int(driver.find_element(
        By.XPATH, '(//span[@class="toolbar-number"][normalize-space()="14"])[1]').text)
    item_products_one_page = driver.find_elements(By.CLASS_NAME, 'product-item-link')
    number_item_products_one_page = int(len(item_products_one_page))
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    button_next = driver.find_element(By.XPATH, '(//a[contains(@title,"Next")])[2]')
    driver.execute_script('arguments[0].scrollIntoView();', button_next)
    button_next.click()
    WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="product-item-link"]')))
    item_products_two_page = driver.find_elements(By.CSS_SELECTOR, '[class="product-item-link"]')
    number_item_products_two_page = int(len(item_products_two_page))
    assert quantity_items == number_item_products_one_page + number_item_products_two_page


def test_page_gear(driver):
    driver.get('https://magento.softwaretestingboard.com/sale.html')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    link_gear_steals = driver.find_element(
        By.XPATH, '//span[normalize-space()="Your best efforts deserve a deal"]')
    driver.execute_script('arguments[0].scrollIntoView();', link_gear_steals)
    link_gear_steals.click()
    text_gear = driver.find_element(By.CLASS_NAME, 'base').text
    assert text_gear == 'Gear'
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="sidebar sidebar-main"]')))
    text_menu = driver.find_element(
        By.CSS_SELECTOR, '[class="sidebar sidebar-main"]').get_attribute('innerText')
    assert text_menu == ("Shop By\nCategory\nBags 14\n"
                         "Fitness Equipment 11\nWatches 9\nBags\nFitness Equipment\nWatches")
    menu_gear = driver.find_element(By.XPATH, '//a[@id="ui-id-6"]//span[contains(text(),"Gear")]')
    actions = ActionChains(driver)
    actions.move_to_element(menu_gear).perform()
    link_bags = driver.find_element(By.ID, 'ui-id-25')
    text_link_page_bags = link_bags.text
    actions.move_to_element(link_bags).click().perform()
    text_page_bags = driver.find_element(By.CLASS_NAME, 'base').text
    assert text_link_page_bags == text_page_bags
    menu_gear = driver.find_element(By.XPATH, '//a[@id="ui-id-6"]//span[contains(text(),"Gear")]')
    actions.move_to_element(menu_gear).perform()
    link_fitness_equipment = driver.find_element(By.ID, 'ui-id-26')
    text_link_fitness_equipment = link_fitness_equipment.text
    actions.move_to_element(link_fitness_equipment).click().perform()
    text_page_fitness_equipment = driver.find_element(By.CLASS_NAME, 'base').text
    assert text_link_fitness_equipment == text_page_fitness_equipment
    menu_gear = driver.find_element(By.XPATH, '//a[@id="ui-id-6"]//span[contains(text(),"Gear")]')
    actions.move_to_element(menu_gear).perform()
    link_watches = driver.find_element(By.ID, 'ui-id-27')
    text_link_watches = link_watches.text
    actions.move_to_element(link_watches).click().perform()
    text_page_watches = driver.find_element(By.CLASS_NAME, 'base').text
    assert text_link_watches == text_page_watches


