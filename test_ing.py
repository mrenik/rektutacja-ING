import pytest
from playwright.sync_api import Page
from datetime import datetime
import os

def test_cookie_consent(page: Page):
    try:
        page.set_default_timeout(60000)
        page.goto("https://www.ing.pl/")  # Zwiększony timeout dla nawigacji

        page.get_by_role("button", name="Dostosuj").click()  # Zwiększony timeout dla kliknięcia
        page.get_by_role("heading", name="Cookies analityczne").click()  # Zwiększony timeout dla kliknięcia
        page.get_by_role("button", name="Zaakceptuj zaznaczone").click()  # Zwiększony timeout dla kliknięcia

        cookies = page.context.cookies()
        target_cookie = next((c for c in cookies if c["name"] == "cookiePolicyGDPR"), None)

        assert target_cookie is not None, f"Cookie nie znalezione"
        assert target_cookie["value"] == "3", f"Oczekiwano cookie z wartością '3', a nie {target_cookie['value']}"

    except Exception as e:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"failed_cookie_consent_{timestamp}.png")
        page.screenshot(path=screenshot_path)
        print(f"Zrobiono screenshot po nieudanym teście: {screenshot_path}")
        raise  # Ponownie zgłoś wyjątek, aby test nadal był oznaczony jako nieudany
