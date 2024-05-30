from enum import Enum
from typing import List

from scripts.config import PREFIX
from scripts.ngrok import get_endpoints


class Command:
    def __init__(self, name: str, description: str, func=None):
        self.name = name
        self.description = description
        self.func = func

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def execute(self) -> None:
        if self.func:
            self.func()


class Commands(Enum):
    HELP = Command(
        "help",
        "Show instructions on how to use this bot.",
        lambda: get_help_response())
    SERV = Command(
        "serv",
        "Show endpoints/servers.",
        lambda: get_endpoints_response())


def get_response(user_input: str) -> str:
    user_input: str = user_input.lower()

    for command in Commands:
        if user_input == command.value.get_name():
            return command.value.execute()

    return get_general_response()


def get_help_response() -> str:
    response: str = ""
    response += insert_heading("books", "Help")
    response += insert_newline(f"**{PREFIX}{Commands.HELP.value.name}**: {Commands.HELP.value.description}")
    response += insert_newline(f"**{PREFIX}{Commands.SERV.value.name}**: {Commands.SERV.value.description}")
    return response.strip()


def get_endpoints_response() -> str:
    endpoints = get_endpoints()
    response: str = ""
    response += insert_heading("satellite", "Endpoints/Servers")
    response += insert_error("No endpoints found.") if not endpoints else insert_list(endpoints)
    return response.strip()


def insert_heading(emoji: str, title: str) -> str:
    return f"\n:{emoji}: **{title}**\n"


def insert_newline(content: str | List = None) -> str:
    if isinstance(content, list):
        return "".join(f"{lst_str}\n" for lst_str in content)
    return f"{content}\n"


def insert_list(lst: List[str]) -> str:
    return "".join(f"{i+1}. {item}\n" for i, item in enumerate(lst))


def insert_error(content: str) -> str:
    return f":robot: {content}\n"


def get_general_response() -> str:
    return f"I do not understand... try **{PREFIX}{Commands.HELP.value}**."
