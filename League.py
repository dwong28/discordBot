import discord
import random
import asyncio
import pprint
from riotwatcher import RiotWatcher, LoLException, error_404
from discord.ext import commands
from botInfo import riot_api_key


# Valid League of Legends Servers
servers = ['br', 'eune', 'euw',
           'kr', 'lan', 'las', 'na',
           'oce', 'ru', 'tr', 'jp']
queues = {'NORMAL': '5v5: Normal Game',
          'BOT': '5v5: Co-Op vs AI',
          'RANKED_SOLO_5x5': '5v5: Solo Queue',
          'RANKED_PREMADE_3x3': '5v5: Ranked Premade',
          'RANKED_PREMADE_5x5': '5v5: Ranked Premade',
          'ODIN_UNRANKED': 'Dominion',
          'RANKED_TEAM_3x3': '3v3: Ranked Teams',
          'RANKED_TEAM_5x5': '5v5: Ranked Teams',
          'NORMAL_3x3': '3v3: Normal Game',
          'BOT_3x3': '3v3: Co-Op vs AI',
          'CAP_5x5': 'Team Builder',
          'ARAM_UNRANKED_5x5': 'ARAM',
          'ONEFORALL_5x5': 'One For All',
          'FIRSTBLOOD_1x1': '1v1 Snowdown',
          'FIRSTBLOOD_2x2': '2v2 Snowdown',
          'SR_6x6': 'Hexakill - SR',
          'URF': 'Ultra Rapid Fire',
          'URF_BOT': 'Ultra Rapid Fire - Co-Op vs AI',
          'NIGHTMARE_BOT': 'Doom Bots',
          'ASCENSION': 'Ascension',
          'HEXAKILL': 'Hexakill - TT',
          'KING_PORO': 'Legend of the Poro King',
          'COUNTER_PICK': 'Nemesis Draft',
          'BILGEWATER': 'Black Market Brawlers',
          'SIEGE': 'Siege',
          'RANKED_FLEX_SR': '5v5 - Flex Queue',
          'RANKED_FLEX_TT': '3v3- Flex Queue'}

borderColors = {'BRONZE': 0XCD7F32,
                'SILVER': 0XBFC1C2,
                'GOLD': 0XD4AF37,
                'PLATINUM': 0X008080,
                'DIAMOND': 0X7DF9FF,
                'MASTER': 0X848482,
                'CHALLENGER': 0XFFDF00}

# Establish Connection to Riot API
session = RiotWatcher(riot_api_key)
print(session.can_make_request())


class League():
    # Trivia Status
    # 0 => Inactive; 1 => Active
    triviaStatus = 0

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

    @commands.command()
    @asyncio.coroutine
    def rank(self, ign: str):
        """Gives Ranked Information for the specified Summoner."""
        try:
            summoner = session.get_summoner(name=ign)
            leagueInfo = session.get_league_entry(summoner_ids=[summoner['id'], ])
            pprint.pprint(summoner)
            pprint.pprint(leagueInfo)
            summonerName = summoner['name']
            summonerId = summoner['id']
            data = discord.Embed(description=formatUnderline("Ranked Information for:") + " " + summonerName,
                                 colour=discord.Colour(value=borderColors[leagueInfo[str(summonerId)][0]['tier']]))
            for q in leagueInfo[str(summonerId)]:
                queueType = queues[q['queue']]
                tier = q['tier']
                division = q['entries'][0]['division']
                lp = q['entries'][0]['leaguePoints']

                data.add_field(name="Queue Type", value=queueType, inline=False)
                data.add_field(name="Division Name", value=q['name'])
                data.add_field(name="Division - Tier", value=tier + " " + division)
                data.add_field(name="League Points", value=str(lp))
                if 'miniSeries' in q['entries'][0]:
                    promoStat = q['entries'][0]['miniSeries']['progress']
                    series = str()
                    for c in promoStat:
                        if c is 'W':
                            series += ":white_check_mark:"
                        if c is 'L':
                            series += ":x:"
                        if c is 'N':
                            series += ":question:"
                    data.add_field(name="Series Status", value=series)

                merits = str()
                if q['entries'][0]['isHotStreak']:
                    merits += ":fire:"
                if q['entries'][0]['isVeteran']:
                    merits += ":medal:"
                if q['entries'][0]['isFreshBlood']:
                    merits += ":star2:"
                if q['entries'][0]['isInactive']:
                    merits += ":skull:"
                if merits:
                    data.add_field(name="Denotations", value=merits)
            yield from self.bot.say(embed=data)

        except LoLException as e:
            if e == error_404:
                yield from self.bot.say(formatBoldItalic("Error: ") + " Summoner " + ign + " not found.")

    @commands.command()
    @asyncio.coroutine
    def trivia(self, string: str):
        """Plays a game of Trivia."""
        if string.lower() == "start":
            if League.triviaStatus == 1:
                yield from self.bot.say("Error: Trivia is started.")

            else:
                yield from self.bot.say("Trivia has started! Name the Champion that speaks each " +
                                        "quote. First to 10 Points wins!")
                League.triviaStatus = 1

                print("Starting")
        elif string == "end":
            League.triviaStatus = 0
            yield from self.bot.say("Ending Trivia.")

            print("Ending")
        else:
            yield from self.bot.say(formatBoldItalic("Error: ") + "Invalid Trivia command")
            print("Error")



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


def formatUnderline(inp: str):
    return "__" + inp + "__"


# Generates a Color for the embedding
def generateColor():
    color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    color = int(color, 16)


def setup(bot):
    bot.add_cog(League(bot))

