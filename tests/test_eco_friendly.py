

def test_add_cart(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.add_cart()
    eco_friendly.check_text_add_cart('S', 'Blue',
                                     'You added Bella Tank to your shopping cart.', '1')


def test_add_compare(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.add_compare()
    eco_friendly.check_text_add_compare('You added product Bella Tank to the comparison list.')


def test_add_wish_list(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.add_wish_list('Customer Login')
    eco_friendly.check_text_wish_list(
        'Bella Tank has been added to your Wish List. Click here to continue shopping.', 'My Wish List')
