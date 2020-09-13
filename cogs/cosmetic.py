import urllib.parse
import requests
import discord
import os
import time

from discord.ext import commands

class cosmetic(commands.Cog):

    def __init__(self, client):
        self.client = client

    # shows solo,duo.squad wins and there win KD
    
                        

        


def setup(bot):
  bot.add_cog(cosmetic(bot))