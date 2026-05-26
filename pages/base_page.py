from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def wait_for_loader_hidden(self) -> None:
        loader = self.page.locator("[data-qa-verified-global-loader]")

        expect(loader).to_be_hidden(timeout=10000)

    def wait_until_page_ready(self) -> None:
        self.page.wait_for_load_state("networkidle")
