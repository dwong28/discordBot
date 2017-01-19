import discord
from discord.ext import commands
import asyncio



class Math():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @asyncio.coroutine
    def add(self, left: int, right: int):
        """Adds 2 Numbers"""
        print("adding")
        yield from self.bot.say((left + right))

    @commands.command()
    @asyncio.coroutine
    def sub(self, left: int, right: int):
        """Subtracts 2 Numbers"""
        print("Subtracting")
        yield from self.bot.say((left - right))

    @commands.command()
    @asyncio.coroutine
    def mult(self, left: int, right: int):
        """Multiplies 2 Numbers"""
        print("Multiplying")
        yield from self.bot.say((left * right))

    @commands.command()
    @asyncio.coroutine
    def div(self, dividend: int, divisor: int):
        """Divides 2 numbers"""
        if divisor == 0:
            yield from self.bot.say("***ERROR: *** Divisor is Zero.")
        else:
            yield from self.bot.say((dividend / divisor))


def setup(bot):
    bot.add_cog(Math(bot))
