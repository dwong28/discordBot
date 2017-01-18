import discord
import leagueCommands
from botInfo import token
from discord.ext import commands
from discord import embeds
import asyncio
description = "test bot"
#client = discord.Client()
commandBot = commands.Bot(command_prefix='!', description=description)

@commandBot.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(commandBot.user.name)
    print(commandBot.user.id)
    print('------')


#@client.event
#@asyncio.coroutine
#def on_message(message):
#    if message.content.startswith('l!serverStats'):
#        leagueCommands.server_status(message.content[1])
#        print(message.content[1])
#    elif message.content.startswith('!add'):
#        add(message.content[1], message.content[2])
#    elif message.content.startswith('!sleep'):
#        yield from client.send_message(message.channel, "Sleeping for 5 secs. Oyasumi~~")
#        yield from asyncio.sleep(5)
#        yield from client.send_message(message.channel, 'Done sleeping')
#    elif message.content.startswith('!eat'):
#        yield from client.send_message(message.channel, "Time to eat! NOM NOM NOM")
#    elif message.content.startswith('!adrian'):
#        yield from client.send_message(message.channel, ':adriangasm:')

@commandBot.command()
@asyncio.coroutine
def add(left: int, right: int):
    """Adds two numbers together."""
    print ("adding")
    yield from commandBot.say((left + right))

@commandBot.command()
@asyncio.coroutine
def status(server: str):
    services = leagueCommands.server_status(server)
    yield from commandBot.say(formatBold(services[0]['name'] + ": ") + services[0]['status'])
    if services[0]['incidents']:
        incident = getIncident(services)
        yield from commandBot.say(formatBoldItalic("Incident: ") + incident)


def formatBold(input: str):
    return "**" + input + "**"

def formatBoldItalic(input: str):
    return "***" + input + "***"
# Gets the incident posted on the game.
# Will only be called if the incidents array is not empty, as to avoid errors
def getIncident(services):
    return services[0]['incidents'][0]['updates'][0]['content']
@commandBot.command()
@asyncio.coroutine
def eat():
    """Eat"""
    yield from commandBot.say("Time to eat! NOM NOM NOM")

@commandBot.command()
@asyncio.coroutine
def joined(member : discord.Member):
    """Says when a member joined."""
    yield from commandBot.say('{0.name} joined in {0.joined_at}'.format(member))

commandBot.run(token)

