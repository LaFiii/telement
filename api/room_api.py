from api.matrix_client import MatrixClient


class RoomApi:
    def __init__(self, matrix_client: MatrixClient) -> None:
        self.matrix_client = matrix_client

    def create_room(self, room_name: str) -> str:
        return self.matrix_client.create_room(room_name)

    def delete_room(self, room_id: str) -> None:
        pass

    def invite_user(self, room_id: str, user_id: str) -> None:
        pass

    def send_message(self, room_id: str, message: str) -> None:
        pass
