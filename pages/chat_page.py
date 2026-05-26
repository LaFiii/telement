from playwright.sync_api import Page, expect

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

    def verify_message_visible(self, message: str, ) -> None:
        message_locator = self.page.locator(f"[data-qa-verified-message-text='{message}']")
        expect(message_locator).to_be_visible()

    def verify_message_delivered(self, message: str) -> None:
        delivered_status = self.page.locator(f"[data-qa-verified-message-status='{message}_delivered']")
        expect(delivered_status).to_be_visible()
