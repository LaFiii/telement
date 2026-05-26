import requests


class MatrixClient:
    def __init__(self, base_url: str, access_token: str) -> None:
        self.base_url = base_url
        self.access_token = access_token

    @property
    def headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.access_token}"
        }

    def create_room(self, room_name: str) -> str:
        response = requests.post(
            f"{self.base_url}/_matrix/client/r0/createRoom",
            headers=self.headers,
            json={
                "name": room_name
            }
        )

        response.raise_for_status()

        return response.json()["room_id"]
