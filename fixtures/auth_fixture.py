import pytest

from utils.config import (BASE_URL, PASSWORD, USERNAME)


@pytest.fixture(scope="session")
def authenticated_page(browser):
    context = browser.new_context()

    page = context.new_page()

    page.goto(BASE_URL)

    page.locator("[data-qa-verified-login-field]").fill(USERNAME)

    page.locator("[data-qa-verified-password-field]").fill(PASSWORD)

    page.locator("[data-qa-verified-login-submit]").click()

    page.wait_for_selector("[data-qa-verified-room-list]")

    yield page

    context.close()
