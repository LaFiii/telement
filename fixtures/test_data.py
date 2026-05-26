from uuid import uuid4


def generate_message() -> str:
    return (
        f"playwright_test_"
        f"{uuid4().hex[:8]}"
    )
