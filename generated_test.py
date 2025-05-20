import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.xe.com/")
    page.get_by_role("button", name="Accept").click()
    page.get_by_text("1.00$").click()
    page.get_by_role("textbox", name="Amount").fill("100")
    page.get_by_role("textbox", name="Amount").press("Enter")
    page.locator("#midmarketFromCurrency").get_by_role("combobox", name="Type to search...").click()
    page.locator("#midmarketFromCurrency").get_by_role("combobox", name="Type to search...").fill("real")
    page.get_by_text("BRL Brazilian Real").click()
    page.locator("#midmarketToCurrency").get_by_role("combobox", name="Type to search...").click()
    page.locator("#midmarketToCurrency").get_by_role("combobox", name="Type to search...").fill("euro")
    page.get_by_text("(Euro Member Countries)").click()
    page.get_by_role("button", name="Convert").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
