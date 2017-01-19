import discord
import random
from botInfo import token
from discord.ext import commands
from riotwatcher import riotwatcher
from discord import embeds
import asyncio
description = "Botting is bad, mmkay??"
#client = discord.Client()
commandBot = commands.Bot(command_prefix='!', description=description)
startupExt = ["Math", "League", "General"]

@commandBot.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(commandBot.user.name)
    print(commandBot.user.id)
    print('------')
    try:
        for ext in startupExt:
            commandBot.load_extension(ext)
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        print('Failed to load extension {}\n{}'.format("Math", exc))





@commandBot.command()
@asyncio.coroutine
def teemo():
    """Teemo."""
    yield from commandBot.say("Teemo is the best!")


@commandBot.command()
@asyncio.coroutine
def riven():
    """Talks about how awesome Riven is"""
    statements = {0: "Riven is amazing",
                  1: "Riven takes mechanical skill.",
                  2: "Riven's lore is so deep.",
                  3: "Riven was the poster child of Noxus.",
                  4: "Riven can bench more than you.",
                  5: "Riven is beautiful.",
                  6: "Riven's kit fits together perfectly.",
                  7: "Riven is the perfect mix of elegance and strength.",
                  8: "What is broken Can be Reforged.",
                  9: "This is why I spend so much time sheath shopping."}
    number = random.randrange(0, 10)
    yield from commandBot.say(statements[number])


@commandBot.command()
@asyncio.coroutine
def yasuo():
    """For the Yas Mains."""
    yield from commandBot.say("I'm a Yasuo Main and I'm Toxic.")


@commandBot.command()
@asyncio.coroutine
def yi():
    """Cowsep I honor you with this."""
    yield from commandBot.say("I WAS IN ALPHA!!! >:O")


@commandBot.command()
@asyncio.coroutine
def nami():
    """This one's for Aly."""
    yield from commandBot.say("I'm the Best Nami.")


@commandBot.command()
@asyncio.coroutine
def say(inp: str):
    """Repeats whatever the user puts in"""
    yield from commandBot.say(inp)


@commandBot.command()
@asyncio.coroutine
def eat():
    """Nom."""
    yield from commandBot.say("Time to eat! NOM NOM NOM")

@commandBot.command()
@asyncio.coroutine
def joined(member : discord.Member):
    """Says when a member joined."""
    yield from commandBot.say('{0.name} joined in {0.joined_at}'.format(member))





commandBot.run(token)

