from enum import Enum
from typing import Dict, List

from scripts.ngrok import get_endpoints
from scripts.config import PREFIX


class Commands(Enum):
    HELP = "help"
    SERV = "serv"


COMMAND_FUNCTIONS: Dict[str, callable] = {
    Commands.HELP.value: lambda: get_help_response(),
    Commands.SERV.value: lambda: get_endpoints_response(),
}


def get_response(user_input: str) -> str:
    user_input: str = user_input.lower()

    if user_input in COMMAND_FUNCTIONS:
        return COMMAND_FUNCTIONS[user_input]()
    else:
        return get_general_response()


def get_help_response() -> str:
    response: str = ""
    response += insert_section("books", "Help")
    response += insert_newline("Use **!dm**\\{command\\} for direct message.")
    response += insert_heading("tools", "Commands")
    response += insert_newline(f"**{PREFIX}{Commands.HELP.value}**: Show this.")
    response += insert_newline(f"**{PREFIX}{Commands.SERV.value}**: Show endpoints/servers.")
    return response.strip()


def get_endpoints_response() -> str:
    endpoints = get_endpoints()
    response: str = ""
    response += insert_section("satellite", "Endpoints/Servers")
    response += insert_error("No endpoints found.") if not endpoints else insert_list(endpoints)
    return response.strip()


def insert_section(emoji: str, title: str) -> str:
    return f":{emoji}: **{title}**\n"


def insert_heading(emoji: str, title: str) -> str:
    return f"\n:{emoji}: **{title}**\n"


def insert_newline(content: str | List = None) -> str:
    if isinstance(content, list):
        return "".join(f"{lst_str}\n" for lst_str in content)
    return f"{content}\n"


def insert_list(lst: List[str]) -> str:
    return "".join(f"`{item}`\n" for item in lst)


def insert_error(content: str) -> str:
    return f":robot: {content}\n"


def get_general_response() -> str:
    return "I do not understand... try **{PREFIX}{Commands.HELP.value}**."
