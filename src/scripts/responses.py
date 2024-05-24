from random import choice
from typing import Dict, List

from scripts.api import get_endpoints

COMMANDS: Dict[str, str] = {
    "help": "Display a list of commands.",
    "serv": "Displays a list of running endpoints/servers."
}


def get_responses(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == "":
        return get_empty_response()
    elif lowered == "help":
        return get_help()
    elif lowered == "serv":
        return get_formatted_endpoints(get_endpoints())
    else:
        return get_general_response()


def format_dict_to_list(items: Dict[str, str]) -> List[str]:
    return [f"{key}: {value}" for key, value in items.items()]


def format_as_markdown(title: str, items: List | Dict) -> str:
    if isinstance(items, Dict):
        items = format_dict_to_list(items)
    formatted_items = "\n".join(items)
    return f":books: **{title}**\n```ruby\n{formatted_items}\n```"


def get_empty_response() -> str:
    return choice(["Try saying something...",
                   "Prompt me with a command..."])


def get_help() -> str:
    return format_as_markdown("Commands", COMMANDS)


def get_formatted_endpoints(endpoints: list) -> str:
    return format_as_markdown("Endpoints/Servers", endpoints)


def get_general_response() -> str:
    return choice(["I do not understand...",
                   "I have not learned that yet...",
                   "Not sure what you mean by that..."])
