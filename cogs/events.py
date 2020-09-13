import urllib.parse
import requests
import discord
import os
import time

from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #Example of an event in a cog.
    @commands.Cog.listener()
    async def on_guild_join(self, guild, ctx):
      await ctx.send("Hey")
      
    #Example of a command in a cog.
    @commands.command()
    async def command(self, ctx):
        await ctx.send("This is an example of a command in a cog!")
      
def setup(bot):
  bot.add_cog(Events(bot))
