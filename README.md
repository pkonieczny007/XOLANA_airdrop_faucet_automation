# XOLANA Airdrop Faucet Automation

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
   git clone https://github.com/TwojUsername/XOLANA_airdrop_faucet_automation.git
   cd XOLANA_airdrop_faucet_automation
