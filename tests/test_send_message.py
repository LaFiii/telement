from pages.chat_page import ChatPage
from fixtures.test_data import generate_message


def test_send_message(authenticated_page, test_room):
    chat_page = ChatPage(authenticated_page)
    message = generate_message()
    chat_page.open_room(test_room["room_name"])

    with authenticated_page.expect_response(
            lambda response:
            "/sync" in response.url
            and response.status == 200
    ):
        chat_page.send_message(message)

    chat_page.verify_message_visible(message)
    chat_page.verify_message_delivered(message)
