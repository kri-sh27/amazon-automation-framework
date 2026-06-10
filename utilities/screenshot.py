import os
from datetime import datetime


def capture(driver, test_name):

    os.makedirs("screenshots", exist_ok=True)

    file_name = (
        f"screenshots/{test_name}_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    )

    driver.save_screenshot(file_name)