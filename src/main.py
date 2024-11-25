import logging

from discord import Client, DMChannel, Forbidden, Intents, Message

from scripts.config import DISC_APP_KEY, PREFIX
from scripts.responses import get_response

# LOG SETUP
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

# BOT SETUP
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)


@client.event
async def on_ready() -> None:
    '''
    This event is called when the bot is ready to start being used.
    '''
    logging.info(f"{client.user} is now running")


# MESSAGE HANDLING
@client.event
async def on_message(message: Message) -> None:
    '''
    This event is called when a message is sent.
    '''
    if not message.content:
        logging.warning("Intent was not set up correctly")
        return

    # Ignore messages that is not intended.
    if not is_dm(message) and not has_prefix(message):
        return

    # Prevent bot from responding to itself.
    if message.author == client.user:
        return

    try:
        log_message(message)
        message.content = clean_message(message)

        await send_message(message)
        await del_message(message)
    except Exception as e:
        logging.error(e)
        await message.channel.send(f"{client.user.mention} is experiencing some issues.")


def is_dm(message: Message) -> bool:
    return isinstance(message.channel, DMChannel)


def has_prefix(message: Message) -> bool:
    return message.content.startswith(PREFIX)


def log_message(message: Message) -> None:
    if is_dm(message):
        logging.info(f"dm:{str(message.author)}: {message.content}")
    else:
        logging.info(f"ch:{str(message.channel)}:{str(message.author)}: {message.content}")


def clean_message(message: Message) -> str:
    message.content = message.content.strip().lower()
    if has_prefix(message):
        message.content = message.content[len(PREFIX):]
    return message.content


async def send_message(message: Message) -> None:
    try:
        await message.channel.send(get_response(message.content))
    except Forbidden as e:
        logging.info(e)
        await message.channel.send(f"{message.author.mention} please enable direct messages from server members.")


async def del_message(message: Message) -> None:
    try:
        # Verify the source due to permission limitations.
        if not isinstance(message.channel, DMChannel):
            await message.delete()
    except Forbidden as e:
        logging.info(e)
        await message.channel.send(f"{client.user.mention} missing permission to delete in {message.channel.mention}.")


def main() -> None:
    client.run(DISC_APP_KEY)


if __name__ == "__main__":
    main()
