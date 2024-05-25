import logging

from discord import Client, Forbidden, Intents, Message

from scripts.config import DISC_APP_KEY, PREFIX, PREFIX_DM
from scripts.responses import get_response

# LOG SETUP
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s\t%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

# BOT SETUP
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)


# STARTUP
@client.event
async def on_ready() -> None:
    logging.info(f"{client.user} is now running")


# MESSAGE HANDLING
@client.event
async def on_message(message: Message) -> None:
    if not message.content:
        logging.warning("Intent was not set up correctly")
        return

    if not message.content.startswith(PREFIX):
        return

    if message.author == client.user:
        return

    channel = str(message.channel)
    username = str(message.author)
    logging.info(f"<{channel}> {username}: {message.content}")

    # Strip prefix.
    message.content = message.content.strip().lower()[len(PREFIX):]
    # Strip dm prefix.
    if dm := message.content.startswith(PREFIX_DM):
        message.content = message.content[len(PREFIX_DM):]

    try:
        await send_message(message, dm)
        await del_message(message)
    except Exception as e:
        logging.error(e)


async def send_message(message: Message, dm: bool) -> None:
    try:
        response = get_response(message.content)
        await message.author.send(response) if dm else await message.channel.send(response)
    except Forbidden as e:
        await message.channel.send(f"{message.author.mention} please enable direct messages from server members.")
        logging.info(e)


async def del_message(message: Message) -> None:
    try:
        await message.delete()
    except Forbidden as e:
        logging.info(e)
        await message.channel.send(f"{client.user.mention} missing permission to delete in {message.channel.mention}.")


def main() -> None:
    client.run(DISC_APP_KEY)


if __name__ == "__main__":
    main()
