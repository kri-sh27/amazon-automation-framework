from pages.base_page import BasePage
from utilities.locator_reader import LocatorReader


class SearchResultsPage(BasePage):

    def select_first_product(self):

        self.click(
            LocatorReader.get(
                "search.first_product"
            )
        )