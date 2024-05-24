import os
from types import MappingProxyType
from typing import Final

from dotenv import load_dotenv

load_dotenv()

VARS = MappingProxyType({
    "discord_secret": os.getenv("discord_secret"),
    "ngrok_secret": os.getenv("ngrok_secret")})

for var, value in VARS.items():
    if value is None:
        raise Exception(f"{var} not found in .env")

PREFIX: Final[str] = "!"
PREFIX_DM: Final[str] = "dm"

DISCORD_SECRET: Final[str] = VARS["discord_secret"]
NGROK_SECRET: Final[str] = VARS["ngrok_secret"]
