import urllib.parse
import requests
import discord
import os
import time

from discord.ext import commands

class Test(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def fnbr(self, ctx, *, arg):
        fortnite = requests.get(f"https://fortnite-api.com/v1/stats/br/v2?name={arg}").json()
        embed = discord.Embed(title=fortnite['data']['account']['name'], color=0x2093C2)
        embed.add_field(name="Account Id:", value=fortnite['data']['account']['id'], inline=False)
        embed.add_field(name="Overall Wins:", value=fortnite['data']['stats']['all']['overall']['wins'], inline=False)
        embed.set_footer(text=fortnite['status'])
        await ctx.send(embed=embed)






def setup(bot):
  bot.add_cog(Test(bot))