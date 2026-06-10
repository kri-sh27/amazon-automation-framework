from pages.base_page import BasePage
from utilities.locator_reader import LocatorReader


class ProductPage(BasePage):

    def get_price(self):

        return self.get_text(
            LocatorReader.get("product.price")
        )

    def add_to_cart_iphone(self):

        self.click(
            LocatorReader.get(
                "product.add_to_cart_iphone"
            )
        )

    def add_to_cart_samsung(self):

        self.click(
            LocatorReader.get(
                "product.add_to_cart_samsung"
            )
        )