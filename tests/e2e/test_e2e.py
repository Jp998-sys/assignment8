# tests/e2e/test_e2e.py

import pytest
from playwright.sync_api import expect


@pytest.mark.e2e
def test_homepage_title(page, fastapi_server):
    page.goto("http://localhost:8000")
    expect(page.locator("h1")).to_have_text("Welcome to a Simple Calculator")


@pytest.mark.e2e
def test_calculator_add(page, fastapi_server):
    page.goto("http://localhost:8000")
    page.fill("#a", "10")
    page.fill("#b", "5")
    page.get_by_role("button", name="Add").click()
    expect(page.locator("#result")).to_have_text("Calculation Result: 15")


@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    page.goto("http://localhost:8000")
    page.fill("#a", "10")
    page.fill("#b", "0")
    page.get_by_role("button", name="Divide").click()
    expect(page.locator("#result")).to_have_text("Error: Cannot divide by zero!")