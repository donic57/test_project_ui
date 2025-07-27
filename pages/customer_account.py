from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import customer_account_locators as loc


class CustomerAccount(BasePage):

    page_url = '/customer/account/create/'

    def fill_login_form(self, first_name, last_name, password, confirm_password, email=None):
        field_first_name = self.find(loc.field_first_name_loc)
        field_last_name = self.find(loc.field_last_name_loc)
        email_address = self.find(loc.email_address_loc)
        field_password = self.find(loc.field_password_loc)
        field_confirm_password = self.find(loc.field_confirm_password_loc)
        button = self.find(loc.button_loc)
        field_first_name.send_keys(first_name)
        field_last_name.send_keys(last_name)
        if email is not None:
            email_address.send_keys(email)
        field_password.send_keys(password)
        field_confirm_password.send_keys(confirm_password)
        button.click()

    def check_text_in_page_bad_add_account_registration(self, text1, text2):
        password_error = self.find(loc.password_error_loc)
        email_address_error = self.find(loc.email_address_error_loc)
        assert password_error.text == text1
        assert email_address_error.text == text2

    def check_text_in_page_add_account_registration(self, text):
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(loc.success_message_loc))
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                loc.success_message_loc,
                'Thank you for registering with Main Website Store.'))
        assert success_message.text == text

    def check_text_account(self, text):
        text_website = self.find(loc.text_website_loc)
        assert text_website.get_attribute('innerText') == text
