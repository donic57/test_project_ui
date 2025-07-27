from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import eco_friendly_page_locators as loc
from selenium.webdriver import ActionChains


class EcoFriendlyPage(BasePage):

    text_one_page = None
    text_two_page = None
    size_text = None
    color_text = None
    text_one = None

    page_url = '/collections/eco-friendly.html'

    def add_cart(self):
        choice_bella_tank = self.find(loc.choice_bella_tank_loc)
        self.text_one_page = self.find(
            loc.text_one_page_loc).text
        actions = ActionChains(self.driver)
        actions.move_to_element(choice_bella_tank).click().perform()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(loc.size_loc))
        size = self.find(loc.size_loc)
        color = self.find(loc.color_loc)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.size_loc))
        size.click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.color_loc))
        color.click()
        button_add_to_cart = self.find(loc.button_add_to_cart_loc)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.button_add_to_cart_loc))
        actions.move_to_element(button_add_to_cart).click().perform()
        self.text_two_page = self.find(loc.text_two_page_loc).text
        self.size_text = self.find(loc.size_text_loc).text
        self.color_text = self.find(loc.color_text_loc).text

    def check_text_add_cart(self, text1, text2, text3, text4):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                loc.data_bind_loc))
        text_add_cart = self.find(loc.data_bind_loc).text
        counter_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                loc.counter_number_loc)).text
        assert self.text_one_page == self.text_two_page
        assert self.size_text == text1
        assert self.color_text == text2
        assert text_add_cart == text3
        assert counter_number == text4

    def add_compare(self):
        choice_bella_tank = self.find(loc.choice_bella_tank_loc)
        actions = ActionChains(self.driver)
        actions.move_to_element(choice_bella_tank).perform()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                loc.button_add_to_compare_loc))
        button_add_to_compare = self.find(loc.button_add_to_compare_loc)
        actions.move_to_element(button_add_to_compare).click(button_add_to_compare).perform()
        self.text_one = self.find(loc.text_one_page_loc).text

    def check_text_add_compare(self, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                loc.text_two_loc))
        text_two = self.find(
            loc.text_two_loc).get_attribute('innerText')
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(loc.data_bind_loc))
        text_add_product = self.find(loc.data_bind_loc).text
        assert self.text_one == text_two
        assert text_add_product == text

    def add_wish_list(self, text):
        email = 'tesstqa@mail.ru'
        password = '12345aa!'
        choice_bella_tank = self.find(loc.choice_bella_tank_loc)
        self.text_one_page = self.find(loc.text_one_page_loc).text
        actions = ActionChains(self.driver)
        actions.move_to_element(choice_bella_tank).perform()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                loc.button_add_wish_list_loc))
        button_add_wish_list = self.find(loc.button_add_wish_list_loc)
        actions.move_to_element(button_add_wish_list).click(button_add_wish_list).perform()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                loc.login_wait_loc))
        text_page_login = self.find(
            loc.text_page_login_loc).text
        assert text_page_login == text
        add_email = self.find(loc.add_email_loc)
        add_password = self.find(loc.add_password_loc)
        add_email.send_keys(email)
        add_password.send_keys(password)
        button_sign_in = self.find(loc.button_sign_in_loc)
        button_sign_in.click()

    def check_text_wish_list(self, text1, text2):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                loc.text_add_wish_list_loc))
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                loc.text_add_wish_list_loc,
                'Bella Tank has been added to your Wish List. Click here to continue shopping.'))
        text_add_wish_list = self.find(loc.text_add_wish_list_loc).text
        text_pege_my_wish_list = self.find(loc.text_pege_my_wish_list_loc).text
        text_two_page = self.find(loc.text_one_page_loc).text
        assert text_add_wish_list == text1
        assert text_pege_my_wish_list == text2
        assert self.text_one_page == text_two_page
