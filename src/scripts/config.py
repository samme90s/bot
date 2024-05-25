import os
from types import MappingProxyType

from dotenv import load_dotenv

load_dotenv()

VARS = MappingProxyType({
    "DISC_APP_KEY": os.getenv("DISC_APP_KEY"),
    "NGROK_API_KEY": os.getenv("NGROK_API_KEY")})

for var, value in VARS.items():
    if value is None:
        raise Exception(f"{var} not found in .env")

PREFIX: str = "!"
PREFIX_DM: str = "dm"

DISC_APP_KEY: str = VARS["DISC_APP_KEY"]
NGROK_API_KEY: str = VARS["NGROK_API_KEY"]
