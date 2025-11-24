

def test_text_page_sale(sale_page):
    sale_page.open_page()
    sale_page.check_text_page_sale("Sale",
                                   "Women's Deals\nHoodies and Sweatshirts\nJackets\n"
                                    "Tees\nBras & Tanks\nPants\nShorts\nMens's Deals\n"
                                    "Hoodies and Sweatshirts\nJackets\nTees\nPants\n"
                                    "Shorts\nGear Deals\nBags\nFitness Equipment")


def test_quantity_items_in_pages(sale_page):
    sale_page.open_page()
    sale_page.page_women_sale('Women Sale')
    sale_page.check_quantity_items_in_pages()
    sale_page.comparison_item_pages()


def test_page_gear(sale_page):
    sale_page.open_page()
    sale_page.click_page_gear()
    sale_page.check_in_text_page_gear("Gear", "Shop By\nCategory\nBags 14\n"
                             "Fitness Equipment 11\nWatches 9\nBags\nFitness Equipment\nWatches")
    sale_page.click_page_bags()
    sale_page.click_page_fitness_equipment()
    sale_page.click_page_watches()
