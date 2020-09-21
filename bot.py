import urllib.parse
import requests
import discord
import os
import time
import pypresence
from pypresence import Presence

from discord.ext import commands

client = commands.Bot(command_prefix = "-")

@client.event
async def on_ready():
    print("Online and Ready")
    status = discord.Activity(type=discord.ActivityType.playing, name="-help")
    await client.change_presence(activity=status)
    rpc = Presence("754666157826506794")
    rpc.connect()
    rpc.update(state="Example", details="Example", large_image="test", start=time.time())
 
@client.command()
async def test(ctx):
    if ctx.channel.is_nsfw():
    ctx.send("Yep")
else:
    ctx.send("Nope")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
client.run(os.environ['DISCORD_TOKEN'])
