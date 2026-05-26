from playwright.sync_api import expect


def wait_for_message(locator, timeout: int = 15000) -> None:
    expect(locator).to_be_visible(timeout=timeout)
