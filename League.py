import discord
from discord.ext import commands
import asyncio
import pprint
from riotwatcher import RiotWatcher
from botInfo import riot_api_key

# Valid League of Legends Servers
servers = ['br', 'eune', 'euw',
           'kr', 'lan', 'las', 'na',
           'oce', 'ru', 'tr', 'jp']

# Establish Connection to Riot API
session = RiotWatcher(riot_api_key)
print(session.can_make_request())

class League():
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @asyncio.coroutine
    def status(self, server: str):
        """States Game Status"""
        inp = server.lower()
        if inp not in servers:
            yield from self.bot.say("***Error: *** Server must be one of the following: ")
            yield from self.bot.say(servers)
        else:
            services = session.get_server_status(server)['services']
            pprint.pprint(services)

            for n in range(0, 4):
                yield from self.bot.say(formatBold(services[n]['name'] + ": ") + services[n]['status'])
                if services[n]['incidents']:
                    incident = getIncident(services[n])
                    yield from self.bot.say(formatBoldItalic("Incident: ") + incident)




# Gets the incident posted on the game.
# Will only be called if the incidents array is not empty, as to avoid errors
def getIncident(service):
    return service['incidents'][0]['updates'][0]['content']

# Formatting for Discord Stuffs
def formatBold(inp: str):
    return "**" + inp + "**"

def formatBoldItalic(inp: str):
    return "***" + inp + "***"

def formatItalic(inp: str):
    return "*" + inp + "*"

def setup(bot):
    bot.add_cog(League(bot))