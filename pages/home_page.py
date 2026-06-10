from pages.base_page import BasePage
from utilities.locator_reader import LocatorReader


class HomePage(BasePage):

    def search(self, product):

        self.type(
            LocatorReader.get("home.search_box"),
            product
        )

        self.click(
            LocatorReader.get("home.search_button")
        )