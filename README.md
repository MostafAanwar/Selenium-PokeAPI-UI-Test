# Selenium PokeAPI UI Test 🧪

This is a QA automation project using Selenium to interact with the [PokéAPI](https://pokeapi.co/) homepage. It opens the site and verifies that the title contains "PokéAPI".

## 🔧 Tech Stack

- Python
- Selenium
- Pytest

## 📁 Folder Structure

```
Selenium-PokeAPI-UI-Test/
├── tests/                  # Contains test cases
├── pages/                  # Page Object Model implementations
├── utils/                  # Base test config
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

## ▶️ How to Run

1. Clone the repo:
```bash
git clone https://github.com/yourusername/Selenium-PokeAPI-UI-Test.git
cd Selenium-PokeAPI-UI-Test
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

4. Run the tests:
```bash
pytest tests/
```
or  
```bash
pytest -s tests/
```

## 🧠 Possible Extensions

- Use [https://pokemondb.net/pokedex](https://pokemondb.net/pokedex) for real UI interaction.
- Add Pokémon detail validation.
- Include negative test cases (e.g., invalid Pokémon names).

---
Created by: FancyPixel – QA Automation with a twist of fun! 🎮
