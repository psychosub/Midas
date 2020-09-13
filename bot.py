import urllib.parse
import requests
import discord
import os
import time

from discord.ext import commands

client = commands.Bot(command_prefix = "-")

@client.event
async def on_ready():
    print("Online and Ready")
    status = discord.Activity(type=discord.ActivityType.playing, name="-help")
    await client.change_presence(activity=status)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
client.run(os.environ['DISCORD_TOKEN'])
