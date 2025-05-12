from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_home(self):
        self.driver.get("https://pokeapi.co/")
