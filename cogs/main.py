import urllib.parse
import requests
import discord
import os
import time

from discord.ext import commands

class main(commands.Cog):

    def __init__(self, client):
        self.client = client

    # shows solo,duo.squad wins and there win KD
    @commands.command()
    async def creatorcode(self, ctx, *, arg):
        fortnite = requests.get(f"https://fortnite-api.com/v2/creatorcode?name={arg}").json()
        embed = discord.Embed(title=fortnite['data']['code'], color=0x2093C2)
        embed.add_field(name="Owner Name", value=fortnite['data']['account']['name'], inline=False)
        embed.add_field(name="Owner ID", value=fortnite['data']['account']['id'], inline=False)
        embed.add_field(name="Status", value=fortnite['data']['status'], inline=False)
        embed.add_field(name="verified", value=fortnite['data']['verified'], inline=False)
        embed.set_thumbnail(url="https://i.pinimg.com/originals/1a/9a/f1/1a9af177bdcd0bd93568e59bb7600cbe.png")
        embed.set_footer(text="By Fortnite-API| @Grenadevisuals")
        await ctx.send(embed=embed)


def setup(bot):
  bot.add_cog(main(bot))