from playwright.sync_api import expect

from pages.chat_page import ChatPage
from fixtures.test_data import generate_message


def test_send_message(authenticated_page, test_room):
    chat_page = ChatPage(authenticated_page)
    message = generate_message()

    chat_page.open_room(test_room["room_name"])
    chat_page.send_message(message)

    expect(chat_page.message_by_text(message)).to_be_visible()
    expect(chat_page.message_delivered_status(message)).to_be_visible()