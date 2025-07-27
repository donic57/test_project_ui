from selenium.webdriver.common.by import By


field_first_name_loc = (By.ID, 'firstname')
field_last_name_loc = (By.ID, 'lastname')
email_address_loc = (By.ID, 'email_address')
field_password_loc = (By.ID, 'password')
field_confirm_password_loc = (By.ID, 'password-confirmation')
button_loc = (By.CSS_SELECTOR, '[class="action submit primary"]')
password_error_loc = (By.ID, 'password-error')
email_address_error_loc = (By.ID, 'email_address-error')
success_message_loc = (By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
text_website_loc = (By.ID, 'maincontent')
