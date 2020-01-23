import json
import discord
import requests
from parsers.monster import MonsterParser


class InvalidCommand(Exception):
    pass


def get_token():
    with open("token.txt", "r") as f:
        return f.read().strip()

# Todo: Implement a help command.


# Category constants
CATEGORY_MONSTERS = "monsters"

# Create the discord client
client = discord.Client()


# Respond to messages.
@client.event
async def on_message(message):
    # So the bot doesn't respond to iteself.
    if message.author == client.user:
        return

    messageTxt = message.content

    # Look for [[<text>]] then parse them as commands
    if messageTxt.startswith("[[") and messageTxt.endswith("]]"):
        try:
            await message.channel.send(handle_message(message))
        except InvalidCommand as e:
            await message.channel.send("Sorry I didn't recognize the command {}".format(str(e)))


# Handlers for the different types of commands
def handle_message(message):
    """
    Generic handler for messages, figures out which handler to call
    based on the request type.
    """
    handlers = {"monster": monster_command}

    command_type, data = message.content.strip("[]").split(":")

    print(command_type)
    print(data)

    if command_type in handlers:
        return handlers[command_type](data)
    else:
        raise InvalidCommand(command_type)


def monster_command( monster ):
    """
    Handles reqeuests for monster data.
    """
    monster_data = make_remote_request(CATEGORY_MONSTERS, monster)
    monster = MonsterParser()
    monster.parse_json(monster_data)

    response = "Found {} they are {} in size".format(monster.name, monster.size)

    return response


# Functions for querying the dnd rest api (http://www.dnd5eapi.co/).
# todo: Support the ability to use local json for homebrew stuff.
def make_remote_request(category, index):
    uri = "http://dnd5eapi.co/api/{}/{}".format(category, index)
    response = requests.get(uri)
    return json.loads(response.content)


# Start the client with the bot's token
client.run(get_token())
