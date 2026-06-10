from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utilities.config_reader import ConfigReader

# def get_driver():

#     options = webdriver.ChromeOptions()

#     options.add_argument("--start-maximized")

#     driver = webdriver.Chrome(
#         service=Service(
#             ChromeDriverManager().install()
#         ),
#         options=options
#     )

#     return driver



def get_driver():

    execution = ConfigReader.get("execution")

    if execution.lower() == "cloud":

        username = ConfigReader.get("username")
        access_key = ConfigReader.get("access_key")

        grid_url = (
            f"https://{username}:{access_key}"
            "@hub.lambdatest.com/wd/hub"
        )

        capabilities = {
            "browserName": "Chrome",
            "browserVersion": "latest",
            "LT:Options": {
                "platformName": "Windows 11",
                "project": "Amazon Assignment",
                "build": "Build-1",
                "name": "Amazon Parallel Test"
            }
        }

        driver = webdriver.Remote(
            command_executor=grid_url,
            options=webdriver.ChromeOptions()
        )

        driver.capabilities.update(capabilities)

        return driver

    else:

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        return webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            ),
            options=options
        )