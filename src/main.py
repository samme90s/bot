import logging

from discord import Client, Forbidden, Intents, Message

from scripts.config import DISCORD_SECRET, PREFIX, PREFIX_DM
from scripts.responses import get_responses

# LOG SETUP
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s\t%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

# BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


# STARTUP
@client.event
async def on_ready() -> None:
    logging.info(f"{client.user} is now running")


# MESSAGE HANDLING
@client.event
async def on_message(message: Message) -> None:
    if not message.content.startswith(PREFIX):
        return

    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content.strip()[len(PREFIX):]
    channel: str = str(message.channel)

    logging.info(f"<{channel}> {username}: {user_message}")
    await send_message(message, user_message)


async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        logging.warning("Message was empty because intents were not enabled properly.")
        return

    if is_dm := user_message.lower().startswith(PREFIX_DM):
        user_message = user_message[len(PREFIX_DM):]
    try:
        response: str = get_responses(user_message)
        await message.author.send(response) if is_dm else await message.channel.send(response)
    except Forbidden as e:
        await message.channel.send(f"{message.author.mention} please enable direct messages from server members.")
        logging.info(e)
    except Exception as e:
        logging.error(e)


def main() -> None:
    client.run(DISCORD_SECRET)


if __name__ == "__main__":
    main()
