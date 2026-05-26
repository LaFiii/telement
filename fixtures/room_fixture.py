import pytest
from uuid import uuid4

from api.matrix_client import MatrixClient


@pytest.fixture()
def test_room():
    room_name = f"autotest_room_{uuid4().hex[:6]}"

    matrix_client = MatrixClient(base_url="https://matrix.org", access_token="token")

    room_id = matrix_client.create_room(room_name)

    yield {
        "room_id": room_id,
        "room_name": room_name,
    }
