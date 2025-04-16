import pytest
from playwright.sync_api import Page


def test_cookie_consent(page: Page):
    page.set_default_timeout(300000)
    page.goto("https://www.ing.pl/") 

    page.get_by_role("button", name="Dostosuj").click()  
    page.get_by_role("heading", name="Cookies analityczne").click() 
    page.get_by_role("button", name="Zaakceptuj zaznaczone").click()  

    cookies = page.context.cookies()
    target_cookie = next((c for c in cookies if c["name"] == "cookiePolicyGDPR"), None)

    assert target_cookie is not None, f"Cookie nie znalezione"
    assert target_cookie["value"] == "3", f"Oczekiwano cookie z wartością '3', a nie {target_cookie['value']}"
