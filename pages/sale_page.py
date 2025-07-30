from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import sale_page_locators as loc
from selenium.webdriver import ActionChains


class SalePage(BasePage):

    quantity_items = None
    number_item_products_one_page = None
    text_gear = None

    page_url = '/sale.html'

    def check_text_page_sale(self, text1, text2):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(loc.base_loc))
        text_sale = self.find(loc.base_loc).text
        assert text_sale == text1
        text_categories_menu = self.find(
            loc.text_categories_menu_loc).get_attribute('innerText')
        assert text_categories_menu == text2

    def page_women_sale(self, text):
        link_women_deals = self.find(loc.link_women_deals_loc)
        self.driver.execute_script('arguments[0].scrollIntoView();', link_women_deals)
        link_women_deals.click()
        text_page_women_sale = self.find(loc.text_page_women_sale_loc).text
        assert text_page_women_sale == text

    def check_quantity_items_in_pages(self):
        self.quantity_items = int(self.find(loc.quantity_items_loc).text)
        item_products_one_page = self.find_all(loc.item_products_one_page_loc)
        self.number_item_products_one_page = int(len(item_products_one_page))
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        button_next = self.find(loc.button_next_loc)
        self.driver.execute_script('arguments[0].scrollIntoView();', button_next)
        button_next.click()

    def comparison_item_pages(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.product_item_link_loc))
        item_products_two_page = self.find_all(loc.product_item_link_loc)
        number_item_products_two_page = int(len(item_products_two_page))
        assert self.quantity_items == self.number_item_products_one_page + number_item_products_two_page

    def click_page_gear(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        link_gear_steals = self.find(loc.link_gear_steals_loc)
        self.driver.execute_script('arguments[0].scrollIntoView();', link_gear_steals)
        link_gear_steals.click()
        self.text_gear = self.find(loc.base_loc).text

    def check_in_text_page_gear(self, text1, text2):
        assert self.text_gear == text1
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(loc.sidebar_sidebar_main_loc))
        text_menu = self.find(
            loc.text_menu_loc).get_attribute('innerText')
        assert text_menu == text2

    def click_page_bags(self):
        menu_gear = self.find(loc.menu_gear_loc)
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_gear).perform()
        link_bags = self.find(loc.link_bags_loc)
        text_link_page_bags = link_bags.text
        actions.move_to_element(link_bags).click().perform()
        text_page_bags = self.find(loc.base_loc).text
        assert text_link_page_bags == text_page_bags

    def click_page_fitness_equipment(self):
        actions = ActionChains(self.driver)
        menu_gear = self.find(loc.menu_gear_loc)
        actions.move_to_element(menu_gear).perform()
        link_fitness_equipment = self.find(loc.link_fitness_equipment_loc)
        text_link_fitness_equipment = link_fitness_equipment.text
        actions.move_to_element(link_fitness_equipment).click().perform()
        text_page_fitness_equipment = self.find(loc.base_loc).text
        assert text_link_fitness_equipment == text_page_fitness_equipment

    def click_page_watches(self):
        actions = ActionChains(self.driver)
        menu_gear = self.find(loc.menu_gear_loc)
        actions.move_to_element(menu_gear).perform()
        link_watches = self.find(loc.link_watches_loc)
        text_link_watches = link_watches.text
        actions.move_to_element(link_watches).click().perform()
        text_page_watches = self.find(loc.base_loc).text
        assert text_link_watches == text_page_watches