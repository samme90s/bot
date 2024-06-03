from requests import get

from scripts.config import NGROK_API_KEY

URL: str = "https://api.ngrok.com"
HEADERS: dict = {
    "authorization": f"Bearer {NGROK_API_KEY}",
    "ngrok-version": "2"
}


def get_endpoints() -> list[str]:
    response = get(url=f"{URL}/endpoints", headers=HEADERS)

    if not response.ok:
        raise Exception(f"{response.status_code}: {response.text}")

    data = response.json()

    return [endpoint["hostport"] for endpoint in data["endpoints"]]
