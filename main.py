#run all of these commands in your cmd / terminal to get the bot up and running and.
#replace the value "YourOwnTokenHere" with your own discord token.
#if you dont have one you can get it from, https://discord.com/developers/docs/intro

#commands to run copy and paste
#pip install nextcord

#the code is made to be easily understood and modified Good Luck on your discord development adventure

#imports
import os
import nextcord
from nextcord.ext import commands

#token
my_secret = os.environ['YourOwnTokenHere']

#client & prefix
client = commands.Bot(command_prefix = "?")

#onready
@client.event
async def on_ready():
  print(f"{client.user} is ready to go, using OpenCord as the base")

#running the bot
client.run(os.environ["YourOwnTokenHere"])