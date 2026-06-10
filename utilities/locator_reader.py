from selenium.webdriver.common.by import By


class LocatorReader:

    locators = {}

    @classmethod
    def load_locators(cls):

        with open("config/locators.properties") as file:

            for line in file:

                if "=" in line:

                    key, value = line.strip().split("=", 1)

                    strategy, locator = value.split("=", 1)

                    by_map = {
                        "id": By.ID,
                        "xpath": By.XPATH,
                        "css": By.CSS_SELECTOR,
                        "name": By.NAME
                    }

                    cls.locators[key] = (
                        by_map[strategy.lower()],
                        locator
                    )

    @classmethod
    def get(cls, key):
        return cls.locators[key]