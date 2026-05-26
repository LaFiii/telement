from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.login_input = page.locator("[data-qa-verified-login-field]")
        self.password_input = page.locator("[data-qa-verified-password-field]")
        self.login_button = page.locator("[data-qa-verified-login-submit]")
        self.room_list = page.locator("[data-qa-verified-room-list]")

    def open(self, base_url: str) -> None:
        self.page.goto(base_url)

    def login(self, username: str, password: str) -> None:
        self.login_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        expect(self.room_list).to_be_visible()
