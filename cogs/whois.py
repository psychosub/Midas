import urllib.parse
import requests
import discord
import os
import time

from discord.ext import commands

class whois(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def whois(self, ctx, *, arg):
        fortnite = requests.get(f"https://fortnite-api.com/v1/stats/br/v2?name={arg}").json()
        embed = discord.Embed(title=fortnite['data']['account']['name'], color=0x2093C2)
        embed.add_field(name="Account Id:", value=fortnite['data']['account']['id'], inline=False)
        embed.add_field(name="Total Wins:", value=fortnite['data']['stats']['all']['overall']['wins'], inline=False)
        embed.add_field(name="Total Deaths:", value=fortnite['data']['stats']['all']['overall']['deaths'], inline=False)
        embed.add_field(name="Total Kills:", value=fortnite['data']['stats']['all']['overall']['kills'], inline=False)
        embed.set_footer(text=fortnite['status'])
        await ctx.send(embed=embed)


    @commands.command()
    async def whoisid(self, ctx, *, arg):
        fortnite = requests.get(f"https://fortnite-api.com/v1/stats/br/v2/{arg}").json()
        embed = discord.Embed(title=fortnite['data']['account']['id'], color=0x2093C2)
        embed.add_field(name="Account Name:", value=fortnite['data']['account']['name'], inline=False)
        embed.add_field(name="Total Wins:", value=fortnite['data']['stats']['all']['overall']['wins'], inline=False)
        embed.add_field(name="Total Deaths:", value=fortnite['data']['stats']['all']['overall']['deaths'], inline=False)
        embed.add_field(name="Total Kills:", value=fortnite['data']['stats']['all']['overall']['kills'], inline=False)
        embed.set_footer(text=fortnite['status'])
        await ctx.send(embed=embed)






def setup(bot):
  bot.add_cog(whois(bot))