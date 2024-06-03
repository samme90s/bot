from enum import Enum

from scripts.config import PREFIX
from scripts.ngrok import get_endpoints


class Command:
    def __init__(self, name: str, description: str, func=None):
        self.name = name
        self.description = description
        self.__func = func

    def execute(self) -> None:
        if self.__func:
            return self.__func()


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
        if user_input == command.value.name:
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


def insert_newline(content: str | list = None) -> str:
    if isinstance(content, list):
        return "".join(f"{lst_str}\n" for lst_str in content)
    return f"{content}\n"


def insert_list(lst: list[str]) -> str:
    return "".join(f"**{i}.** {item}\n" for i, item in enumerate(lst, start=1))


def insert_error(content: str) -> str:
    return f":robot: {content}\n"


def get_general_response() -> str:
    return f"I do not understand... try **{PREFIX}{Commands.HELP.value.name}**."
