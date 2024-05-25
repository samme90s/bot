from typing import List

from requests import get

from scripts.config import NGROK_API_KEY

URL: str = "https://api.ngrok.com/endpoints"
HEADERS: dict = {
    "authorization": f"Bearer {NGROK_API_KEY}",
    "ngrok-version": "2"
}


def get_endpoints() -> List[str]:
    response = get(url=URL, headers=HEADERS)

    if not response.ok:
        raise Exception(f"{response.status_code}: {response.text}")

    data = response.json()

    return [endpoint["hostport"] for endpoint in data["endpoints"]]
