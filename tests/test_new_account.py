from faker import Faker


def test_new_account_bad_registration(account_page):
    account_page.open_page()
    account_page.fill_login_form('test', 'test',
                               '53535fsdfsdf', '53535fsdfsdf')
    account_page.check_text_in_page_bad_add_account_registration('Minimum of different classes of '
                                                       'characters in password is 3. Classes of '
                                                       'characters: Lower Case, Upper Case, Digits, '
                                                       'Special Characters.',
                                                       'This is a required field.')


def test_new_account_success(account_page):
    faker = Faker().email()
    account_page.open_page()
    account_page.fill_login_form('test', 'test',
                               '53535fsdfsdf!', '53535fsdfsdf!', faker)
    account_page.check_text_in_page_add_account_registration(
        'Thank you for registering with Main Website Store.')


def test_check_text_account(account_page):
    account_page.open_page()
    account_page.check_text_account('Create New Customer Account\nPersonal '
                                    'Information\nFirst Name\nLast Name\nSign-in '
                                    'Information\nEmail\nPassword\nPassword Strength: '
                                    'No Password\nConfirm Password\nCreate an Account')
