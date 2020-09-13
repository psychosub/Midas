import urllib.parse
import requests
import discord
import os
import time

from discord.ext import commands

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def newsbr(self, ctx):
        fortnite = requests.get("https://fortnite-api.com/v2/news/br").json()
        embed = discord.Embed(title="Fortnite BR News", color=0x2093C2)
        embed.set_image(url=fortnite["data"]["image"])
        embed.set_footer(text="Thanks For Using Lynx | @Grenadevisuals", icon_url='https://cdn.discordapp.com/attachments/748585359335489596/749286321109073930/H3IcPDkt_400x400.jpg')
        await ctx.send(embed=embed)


    @commands.command()
    async def newscreative(self, ctx):
        fortnite = requests.get("https://fortnite-api.com/v2/news/creative").json()
        embed = discord.Embed(title="Fortnite Creative News", color=0x2093C2)
        embed.set_image(url=fortnite["data"]["image"])
        embed.set_footer(text="Thanks For Using Lynx | @Grenadevisuals", icon_url='https://cdn.discordapp.com/attachments/748585359335489596/749286321109073930/H3IcPDkt_400x400.jpg')
        await ctx.send(embed=embed)







def setup(bot):
  bot.add_cog(Commands(bot))