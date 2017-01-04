import discord
from botInfo import token
from discord.ext import commands
import asyncio

client = discord.Client()


@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = yield from client.send_message(message.channel, 'Calculating messages...')
        asyncio.ensure_future()
        for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        yield from client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        yield from client.send_message(message.channel, "Sleeping for 5 secs. Oyasumi~~")
        yield from asyncio.sleep(5)
        yield from client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!eat'):
        yield from client.send_message(message.channel, "Time to eat! NOM NOM NOM")
    elif message.content.startswith('!adrian'):
        yield from client.send_message(message.channel, ':adriangasm:')

client.run(token)

