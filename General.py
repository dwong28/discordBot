from discord.ext import commands
import asyncio
import random
class General():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @asyncio.coroutine
    def ateBall(self, question: str):
        """Ask the Magic Ate Ball."""
        responses = {0: "It is certain.", 1: "It is decidedly so.", 2: "Without a doubt.", 3: "Yes, definitely.",
                     4: "You may rely on it.", 5: "As I see it, yes.", 6: "Most Likely.", 7: "Outlook good.",
                     8: "Yes.", 9: "Signs point to yes.", 10: "Reply hazy. Try again.", 11: "Ask again later.",
                     12: "Better not tell you now.", 13: "Cannot Predict Now", 14: "Concentrate and ask again",
                     15: "Don't count on it.", 16: "My reply is No.", 17: "My sources say No.",
                     18: "Outlook not so good.", 19: "Very Doubtful."}
        number = random.randrange(0, 20)
        yield from self.bot.say(responses[number])

def setup(bot):
    bot.add_cog(General(bot))
