from enum import Enum
from random import choice
from typing import Dict, List

from scripts.api import get_endpoints


class Commands(Enum):
    HELP = "help"
    SERV = "serv"


COMMANDS: Dict[Commands, str] = {
    Commands.HELP.value: "List commands.",
    Commands.SERV.value: "List running endpoints/servers."
}

COMMAND_FUNCTIONS = {
    Commands.HELP.value: lambda: format_help_message(COMMANDS),
    Commands.SERV.value: lambda: format_endpoints_message(get_endpoints()),
}


def get_responses(user_input: str) -> str:
    lower: str = user_input.lower()

    if lower == "":
        return get_empty_response()
    elif lower in COMMAND_FUNCTIONS:
        return COMMAND_FUNCTIONS[lower]()
    else:
        return get_general_response()


def format_help_message(commands: Dict[Commands, str]) -> str:
    return concatenate_with_newline([
        get_heading("books", "Help"),
        "Use **!dm**\\{command\\} for direct message.",
        get_as_md({command: description for command, description in commands.items()})])


def format_endpoints_message(endpoints: list) -> str:
    return concatenate_with_newline([
        get_heading("satellite", "Endpoints/Servers"),
        get_as_md(endpoints)])


def get_as_md(items: List | Dict) -> str:
    if isinstance(items, Dict):
        items = format_dict_to_list(items)
    return f"```ruby\n{"\n".join(items)}```"


def format_dict_to_list(items: Dict[str, str]) -> List[str]:
    return [f"{key}: {value}" for key, value in items.items()]


def get_heading(emoji: str, title: str) -> str:
    return f":{emoji}: **{title}**"


def concatenate_with_newline(strings: List[str]) -> str:
    return "\n".join(strings)


def get_empty_response() -> str:
    return choice(["Try saying something...",
                   "Prompt me with a command..."])


def get_general_response() -> str:
    return choice(["I do not understand...",
                   "I have not learned that yet...",
                   "Not sure what you mean by that..."])
