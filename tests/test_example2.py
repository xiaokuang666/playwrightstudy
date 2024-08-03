import pytest
from playwright.sync_api import Page, Playwright, sync_playwright, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("before the test runs")

    # Assertions use the expect API.

    yield

    print("after the test runs")


def test_main_navigation(page: Page, playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    expect(page.get_by_placeholder("What needs to be done?")).to_be_visible()
    page.get_by_role("link", name="real TodoMVC app.").click()
    expect(page.get_by_role("link", name="View on GitHub")).to_be_visible()
    page.get_by_role("link", name="View on GitHub").click()




    # ---------------------
    context.close()
    browser.close()

