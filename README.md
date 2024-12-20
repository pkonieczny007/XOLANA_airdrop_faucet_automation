# XOLANA_airdrop_faucet_automation
XOLANA Airdrop Faucet Automation
Opis projektu
XOLANA Airdrop Faucet Automation to skrypt w Pythonie, który automatyzuje proces interakcji z faucetem XOLANA, dostępnym na stronie https://xolana.xen.network/web_faucet. Skrypt umożliwia regularne zgłaszanie żądań airdropu SOL poprzez podanie adresu portfela, kliknięcie przycisku i odczytanie komunikatów ze strony. W przypadku błędów lub ograniczeń czasowych, skrypt inteligentnie dostosowuje czas oczekiwania, aby zoptymalizować proces.

Funkcjonalności
Automatyczne żądanie airdropu:

Wprowadza adres portfela i wysyła żądanie airdropu.
Odczytuje komunikaty ze strony, takie jak:
Sukces: "Transaction confirmed. 5 SOL sent."
Błąd: "Error: Please wait X minutes before requesting again."
Dynamiczne zarządzanie czasem oczekiwania:

Skrypt rozpoznaje czas podany w komunikacie i dostosowuje czas oczekiwania przed kolejną próbą.
Bezobsługowy tryb pracy:

W pełni zautomatyzowany proces dzięki wykorzystaniu biblioteki Selenium oraz WebDriver Manager.
Łatwość konfiguracji:

Prosta konfiguracja, automatyczne zarządzanie WebDriverem przy użyciu webdriver_manager.
Obsługa błędów:

Skrypt wyświetla czytelne komunikaty w przypadku problemów z połączeniem, strukturą strony lub innymi nieprzewidzianymi sytuacjami.
Wymagania systemowe
Python 3.7 lub nowszy
Przeglądarka Google Chrome
Zainstalowane biblioteki:
selenium
webdriver-manager
Instalacja
Sklonuj repozytorium:

bash
Skopiuj kod
git clone https://github.com/TwojUsername/XOLANA_airdrop_faucet_automation.git
cd XOLANA_airdrop_faucet_automation
Zainstaluj wymagane biblioteki:

bash
Skopiuj kod
pip install -r requirements.txt
Jak uruchomić?
Uruchom skrypt:

bash
Skopiuj kod
python airdrop_faucet_automation.py
Skrypt automatycznie rozpocznie żądanie airdropu dla podanego adresu portfela.

Pliki w repozytorium
airdrop_faucet_automation.py — główny skrypt automatyzujący proces.
README.md — dokumentacja projektu.
requirements.txt — lista wymaganych bibliotek.
Używane technologie
Python — język programowania do automatyzacji.
Selenium — biblioteka do automatyzacji interakcji z przeglądarką.
WebDriver Manager — automatyczne zarządzanie WebDriverami.
Przestrogi
Przestrzeganie zasad strony:
Upewnij się, że używanie automatyzacji jest zgodne z regulaminem strony XOLANA.
Bezpieczeństwo klucza prywatnego:
Nie przechowuj klucza prywatnego ani innych wrażliwych danych w skrypcie.
Plan rozwoju
Dodanie możliwości logowania do pliku, aby śledzić historię żądań.
Integracja z API w celu monitorowania stanu portfela.
Rozszerzenie obsługi błędów o bardziej zaawansowane przypadki.
Licencja
Ten projekt jest udostępniany na licencji MIT. Szczegóły w pliku LICENSE.

Zapraszamy do zgłaszania błędów i sugestii! 😊
