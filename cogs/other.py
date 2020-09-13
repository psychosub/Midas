import urllib.parse
import requests
import discord
import os
import time

from discord.ext import commands

class other(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def shop(self, ctx):
        embed = discord.Embed(title="Fortnite Item Shop", color=0x2093C2)
        embed.set_image(url="https://api.nitestats.com/v1/shop/image")
        embed.set_footer(text="By Nitestats API | @Grenadevisuals")
        await ctx.send(embed=embed)

    @commands.command()
    async def map(self, ctx):
        embed = discord.Embed(title="Fortnite Map", color=0x2093C2)
        embed.set_image(url="https://media.fortniteapi.io/images/map.png?showPOI=true")
        embed.set_footer(text="By fortniteAPI | @Grenadevisuals")
        await ctx.send(embed=embed)
     # same as map but without poi names
    @commands.command()
    async def mapclear(self, ctx):
        embed = discord.Embed(title="Fortnite Map", color=0x2093C2)
        embed.set_image(url="https://media.fortniteapi.io/images/map.png?showPOI=false")
        embed.set_footer(text="By fortniteAPI | @Grenadevisuals")
        await ctx.send(embed=embed)


    @commands.command()
    async def export(self, ctx, *, arg):
        embed = discord.Embed(title="Fortnite Export", color=0x2093C2)
        embed.set_image(url=f"https://benbotfn.tk/api/v1/exportAsset?path={arg}&lang=en&noVariants=false&rawIcon=false")
        embed.set_footer(text="By BenBot API | @Grenadevisuals")
        await ctx.send(embed=embed)


    @commands.command()
    async def avatar(self, ctx, *, arg):
        fortnite = requests.get(f"https://benbotfn.tk/api/v1//cosmetics/br/search?name={arg}").json()
        embed = discord.Embed(title=fortnite['name'], color=0x2093C2)
        embed.set_image(url=fortnite["icons"]["icon"])
        embed.set_footer(text="By Fortnite-API| @Grenadevisuals")
        await ctx.send(embed=embed)






def setup(bot):
  bot.add_cog(other(bot))