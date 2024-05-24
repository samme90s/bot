
from discord import Client, Intents, Message

from scripts.config import DISCORD_SECRET, PREFIX
from scripts.responses import get_responses

# BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("Message was empty because intents were not enabled properly.")
        return

    if is_private := user_message[0] == "?":
        user_message = user_message[1:]

    try:
        response: str = get_responses(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# STARTUP
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running")


# MESSAGE HANDLING
@client.event
async def on_message(message: Message) -> None:
    if not message.content.startswith(PREFIX):
        return

    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content[len(PREFIX):]
    channel: str = str(message.channel)

    print(f"<{channel}> {username}: {user_message}")
    await send_message(message, user_message)


def main() -> None:
    client.run(DISCORD_SECRET)


if __name__ == "__main__":
    main()
