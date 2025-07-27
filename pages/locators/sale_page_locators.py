from selenium.webdriver.common.by import By


base_loc = (By.CLASS_NAME, 'base')
text_categories_menu_loc = (By.CLASS_NAME, 'categories-menu')
link_women_deals_loc = (By.CSS_SELECTOR, '[class="more button"]')
text_page_women_sale_loc = (By.XPATH, '//span[normalize-space()="Women Sale"]')
quantity_items_loc = (By.XPATH, '(//span[@class="toolbar-number"][normalize-space()="14"])[1]')
item_products_one_page_loc = (By.CLASS_NAME, 'product-item-link')
button_next_loc = (By.XPATH, '(//a[contains(@title,"Next")])[2]')
product_item_link_loc = (By.CSS_SELECTOR, '[class="product-item-link"]')
link_gear_steals_loc = (By.XPATH, '//span[normalize-space()="Your best efforts deserve a deal"]')
sidebar_sidebar_main_loc = (By.CSS_SELECTOR, '[class="sidebar sidebar-main"]')
text_menu_loc = (By.CSS_SELECTOR, '[class="sidebar sidebar-main"]')
menu_gear_loc = (By.XPATH, '//a[@id="ui-id-6"]//span[contains(text(),"Gear")]')
link_bags_loc = (By.ID, 'ui-id-25')
link_fitness_equipment_loc = (By.ID, 'ui-id-26')
link_watches_loc = (By.ID, 'ui-id-27')