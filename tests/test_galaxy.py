from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from utilities.config_reader import ConfigReader


def test_galaxy(driver):

    driver.get(
        ConfigReader.get("url")
    )

    HomePage(driver).search("Samsung Galaxy")

    SearchResultsPage(driver).select_first_product()

    product = ProductPage(driver)

    price = product.get_price()

    print(f"\nGALAXY PRICE = {price}")

    product.add_to_cart_samsung()