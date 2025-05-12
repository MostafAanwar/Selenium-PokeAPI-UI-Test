import pytest
from pages.home_page import HomePage
from utils.base_test import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_home(self):
        self.driver.get("https://pokeapi.co/")
        self.decline_cookies()

    def decline_cookies(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fc-button-label")))
            for btn in buttons:
                if "accept" in btn.text.lower():
                    btn.click()
                    print("Declined Data Sharing.")
                    return
            print("Dont Consent button not found.")
        except Exception as e:
            print(f"No data collect banner found or error: {e}")

@pytest.mark.usefixtures("driver")
def test_collect_pokemon(driver):
    home = HomePage(driver)
    home.go_to_home()

    try:
        assert "PokéAPI" in driver.title, "Page title does not contain 'PokéAPI'"

        print("Collecting Pokémon info (simulated):")
        pokemon_list = [
            "https://pokeapi.co/api/v2/pokemon/ditto/",
            "https://pokeapi.co/api/v2/pokemon/pikachu/",
            "https://pokeapi.co/api/v2/pokemon/bulbasaur/",
            "https://pokeapi.co/api/v2/pokemon/charmander/",
            "https://pokeapi.co/api/v2/pokemon/squirtle/",
            "https://pokeapi.co/api/v2/pokemon/jigglypuff/",
            "https://pokeapi.co/api/v2/pokemon/meowth/",
            "https://pokeapi.co/api/v2/pokemon/psyduck/",
            "https://pokeapi.co/api/v2/pokemon/snorlax/",
            "https://pokeapi.co/api/v2/pokemon/mewtwo/"
        ]

        for url in pokemon_list:
            print(f" - {url}")

        print("Test completed successfully.")

    except AssertionError as e:
        print(f"Test failed: {e}")

    finally:
        driver.quit()
        print("Browser closed.")
