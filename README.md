# XOLANA Airdrop Faucet Automation

# XOLANA Airdrop Faucet Automation

## Project Description

**XOLANA Airdrop Faucet Automation** is a Python script that automates interactions with the XOLANA faucet available at [https://xolana.xen.network/web_faucet](https://xolana.xen.network/web_faucet). The script allows users to regularly request SOL airdrops by entering a wallet address, clicking a button, and reading messages from the website. In case of errors or time restrictions, the script intelligently adjusts the waiting time to optimize the process.

---

## Features

- **Automated Airdrop Requests**:
  - Enters the wallet address and submits an airdrop request.
  - Reads website messages, such as:
    - Success: `"Transaction confirmed. 5 SOL sent."`
    - Error: `"Error: Please wait X minutes before requesting again."`

- **Dynamic Waiting Time Management**:
  - Adjusts the waiting time based on the website message.

- **Fully Automated Workflow**:
  - Leverages Selenium and WebDriver Manager for seamless automation.

- **Ease of Configuration**:
  - Simple setup with automatic WebDriver management using `webdriver_manager`.

- **Error Handling**:
  - Provides clear messages in case of connectivity issues, page structure changes, or other unexpected situations.

---

## System Requirements

- Python 3.7 or later
- Google Chrome browser
- Installed libraries:
  - `selenium`
  - `webdriver-manager`

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/pkonieczny007/XOLANA_airdrop_faucet_automation.git
   cd XOLANA_airdrop_faucet_automation



2. **Install the required libraries:
```bash
pip install -r requirements.txt
```
3. **Run the script:
```bash
python airdrop_faucet_automation.py
```

## Opis projektu

**XOLANA Airdrop Faucet Automation** to skrypt w Pythonie, który automatyzuje proces interakcji z faucetem XOLANA, dostępnym na stronie [https://xolana.xen.network/web_faucet](https://xolana.xen.network/web_faucet). Skrypt umożliwia regularne zgłaszanie żądań airdropu SOL poprzez podanie adresu portfela, kliknięcie przycisku i odczytanie komunikatów ze strony. W przypadku błędów lub ograniczeń czasowych, skrypt inteligentnie dostosowuje czas oczekiwania, aby zoptymalizować proces.

---

## Funkcjonalności

- **Automatyczne żądanie airdropu**:
  - Wprowadza adres portfela i wysyła żądanie airdropu.
  - Odczytuje komunikaty ze strony:
    - Sukces: `"Transaction confirmed. 5 SOL sent."`
    - Błąd: `"Error: Please wait X minutes before requesting again."`

- **Dynamiczne zarządzanie czasem oczekiwania**:
  - Skrypt rozpoznaje czas podany w komunikacie i dostosowuje czas oczekiwania przed kolejną próbą.

- **Bezobsługowy tryb pracy**:
  - W pełni zautomatyzowany proces dzięki wykorzystaniu biblioteki Selenium oraz WebDriver Manager.

- **Łatwość konfiguracji**:
  - Prosta konfiguracja i automatyczne zarządzanie WebDriverem za pomocą `webdriver_manager`.

- **Obsługa błędów**:
  - Skrypt wyświetla czytelne komunikaty w przypadku problemów z połączeniem, strukturą strony lub innymi nieprzewidzianymi sytuacjami.

---

## Wymagania systemowe

- Python 3.7 lub nowszy
- Przeglądarka Google Chrome
- Zainstalowane biblioteki:
  - `selenium`
  - `webdriver-manager`

---

## Instalacja

1. **Sklonuj repozytorium**:
   ```bash
   git clone https://github.com/pkonieczny007/XOLANA_airdrop_faucet_automation.git
   cd XOLANA_airdrop_faucet_automation
2. **Zainstaluj wymagane biblioteki:
```bash
pip install -r requirements.txt
```
3. **Uruchom skrypt:
```bash
python airdrop_faucet_automation.py
```


