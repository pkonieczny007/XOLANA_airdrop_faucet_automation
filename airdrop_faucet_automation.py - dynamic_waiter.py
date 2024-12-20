import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Konfiguracja przeglądarki w trybie bezgłowym (headless)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Ścieżka do drivera Chrome, użyj webdriver_manager do automatycznego pobrania
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def get_faucet():
    try:
        # Otwórz stronę faucet
        driver.get('https://xolana.xen.network/web_faucet')
        
        # Znajdź pole do wprowadzenia adresu i wpisz adres
        address_input = driver.find_element(By.ID, 'pubkey')
        address_input.send_keys('5T3UojqYFH6hM1ASJDpzJJ5k1Ke54UCMxHWTm9a68S7e')

        # Znajdź przycisk "Submit" i kliknij
        submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        submit_button.click()

        # Czekaj na wynik
        time.sleep(5)  # Oczekiwanie na odpowiedź z serwera

        # Sprawdź wynik transakcji
        status_text = driver.find_element(By.ID, 'status').text

        if "Transaction confirmed. 5 SOL sent." in status_text:
            print("Transakcja udana. 5 SOL zostało wysłane.")
            return True
        elif "Error: Please wait" in status_text:
            print("Faucet nie jest jeszcze dostępny. Musisz poczekać.")
            return False
        else:
            print("Wystąpił błąd.")
            return False
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return False

def main():
    while True:
        # Wywołaj funkcję get_faucet i sprawdź czy się udało
        success = get_faucet()
        
        # Jeżeli się nie udało, odczekaj godzinę i spróbuj ponownie
        if not success:
            print("Spróbuj ponownie za godzinę.")
            time.sleep(3600)  # Czekaj 1 godzinę (3600 sekund)

# Uruchom skrypt
if __name__ == '__main__':
    main()

# Zakończ pracę drivera
driver.quit()
