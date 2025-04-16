# Testy Funkcjonalne Strony ING

Ten projekt zawiera zestaw automatycznych testów funkcjonalnych, które weryfikują kluczowe aspekty działania strony internetowej ING. Testy te zostały stworzone przy użyciu nowoczesnych narzędzi do automatyzacji przeglądarek: Pytest i Playwright.

## Cel Projektu

Celem tego projektu jest zapewnienie wysokiej jakości i niezawodności strony internetowej ING poprzez automatyczne sprawdzanie jej funkcjonalności. Automatyczne testy pozwalają na szybkie i efektywne wykrywanie potencjalnych problemów, co przyczynia się do lepszego doświadczenia użytkowników.

## Technologie Użyte

* **Python:** Popularny język programowania, użyty do napisania testów.
* **Pytest:** Framework do tworzenia i uruchamiania testów w Pythonie.
* **Playwright:** Biblioteka firmy Microsoft do automatyzacji przeglądarek internetowych (Chromium, Firefox, Webkit).
* **GitHub Actions:** Platforma do automatyzacji procesów CI/CD (Continuous Integration/Continuous Delivery), używana do automatycznego uruchamiania testów.

## Jak Uruchomić Testy

Projekt ten zawiera instrukcje, jak uruchomić testy zarówno lokalnie na komputerze, jak i w ramach zautomatyzowanego potoku CI/CD na platformie GitHub.

### Uruchomienie Lokalnie

Aby uruchomić testy na swoim komputerze, wykonaj następujące kroki:

1.  Upewnij się, że masz zainstalowany **Python 3.x**.
2.  Pobierz kod projektu z repozytorium GitHub.
3.  Zainstaluj `pytest` i `playwright` poleceniem `pip install pytest playwright`.
4.  Zainstaluj przeglądarki potrzebne do testów, uruchamiając polecenie `playwright install`.
5.  Uruchom testy, używając polecenia `pytest test_ing.py --browser <nazwa_przeglądarki>` (zamiast `<nazwa_przeglądarki>` wpisz `chromium`, `firefox` lub `webkit`).

    Na przykład, aby uruchomić testy na przeglądarce Firefox, użyj polecenia:
    ```bash
    pytest test_ing.py --browser firefox
    ```

### Automatyczne Uruchamianie w Potoku CI/CD (GitHub Actions)

Projekt jest skonfigurowany do automatycznego uruchamiania testów przy każdej zmianie w kodzie (push) oraz przy tworzeniu lub aktualizacji propozycji zmian (pull request) na platformie GitHub.

Konfiguracja ta znajduje się w pliku `.github/workflows/main.yml`. Dzięki temu, po każdej modyfikacji kodu, testy są automatycznie uruchamiane na różnych przeglądarkach (Chromium, Firefox, Webkit) w środowisku GitHub.

Wyniki tych automatycznych testów można zobaczyć w zakładce "Actions" w repozytorium GitHub.

---
