import urllib.parse
import requests
import discord
import os
import time

from discord.ext import commands

class stats(commands.Cog):

    def __init__(self, client):
        self.client = client

    # shows solo,duo.squad wins and there win KD
    @commands.command()
    async def stats(self, ctx, *, arg):
        fortnite = requests.get(f"https://fortnite-api.com/v1/stats/br/v2?name={arg}").json()
        embed = discord.Embed(title=fortnite['data']['account']['name'], color=0x2093C2)
        embed.add_field(name="Solo Wins:", value=fortnite['data']['stats']['all']['solo']['wins'], inline=False)
        embed.add_field(name="Duo Wins", value=fortnite['data']['stats']['all']['duo']['wins'], inline=False)
        embed.add_field(name="Squad Wins", value=fortnite['data']['stats']['all']['squad']['wins'], inline=False)
        embed.add_field(name="KD", value=fortnite['data']['stats']['all']['overall']['kd'], inline=False)
        embed.set_thumbnail(url="https://i.pinimg.com/originals/1a/9a/f1/1a9af177bdcd0bd93568e59bb7600cbe.png")
        embed.set_footer(text="By Fortnite-API| @Grenadevisuals")
        await ctx.send(embed=embed)




    # shows solo,duo.squad wins and there win KD WITH ID
    @commands.command()
    async def statsid(self, ctx, *, arg):
        fortnite = requests.get(f"https://fortnite-api.com/v1/stats/br/v2/{arg}").json()
        embed = discord.Embed(title=fortnite['data']['account']['name'], color=0x2093C2)
        embed.add_field(name="Solo Wins:", value=fortnite['data']['stats']['all']['solo']['wins'], inline=False)
        embed.add_field(name="Duo Wins", value=fortnite['data']['stats']['all']['duo']['wins'], inline=False)
        embed.add_field(name="Squad Wins", value=fortnite['data']['stats']['all']['squad']['wins'], inline=False)
        embed.add_field(name="KD", value=fortnite['data']['stats']['all']['overall']['kd'], inline=False)
        embed.set_thumbnail(url="https://i.pinimg.com/originals/1a/9a/f1/1a9af177bdcd0bd93568e59bb7600cbe.png")
        embed.set_footer(text="By Fortnite-API| @Grenadevisuals")
        await ctx.send(embed=embed)





def setup(bot):
  bot.add_cog(stats(bot))