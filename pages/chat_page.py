from playwright.sync_api import Page, Locator

from pages.base_page import BasePage


class ChatPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.message_input = page.locator("[data-qa-verified-message-input]")
        self.send_button = page.locator("[data-qa-verified-send-message-button]")

    def open_room(self, room_name: str) -> None:
        self.page.locator(f"[data-qa-verified-room-item='{room_name}']").click()

    def send_message(self, message: str) -> None:
        self.message_input.fill(message)
        self.send_button.click()

    def message_by_text(self, message: str) -> Locator:
        return self.page.locator(f"[data-qa-verified-message-text='{message}']")

    def message_delivered_status(self, message: str) -> Locator:
        return self.page.locator(f"[data-qa-verified-message-status='{message}_delivered']")