from selenium import webdriver
import json
from selenium.webdriver.firefox.service import Service


class BaseTestCase:
    def __init__(self):
        # Set the path to the WebDriver executable (e.g., Firefox)
        service = Service()
        options = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(service=service, options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # Set a default wait time
        with open("config.json", "r") as config_file:
            config_data = json.load(config_file)
        self.url = config_data["url"]
        self.email_address = config_data["email"]

    def tearDown(self):
        self.driver.quit()
