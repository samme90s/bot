from typing import Dict

from requests import get

from scripts.config import NGROK_SECRET

URL: str = "https://api.ngrok.com/endpoints"
HEADERS: dict = {
    "authorization": f"Bearer {NGROK_SECRET}",
    "ngrok-version": "2"
}


def get_endpoints() -> Dict[str, str]:
    response = get(
        url=URL,
        headers=HEADERS)

    if not response.ok:
        raise Exception(f"{response.status_code}: {response.text}")

    data = response.json()
    selected_data: Dict[str, str] = {}
    for endpoint in data["endpoints"]:
        selected_data[endpoint["proto"]] = endpoint["hostport"]

    return selected_data


if __name__ == "__main__":
    print(get_endpoints())
