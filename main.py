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
from nextcord import Member
from nextcord.ext.commands import has_permissions, MissingPermissions
import random

#embedcolor
color = 0xffffff

#token
my_secret = os.environ['YourOwnTokenHere']

#client & prefix
client = commands.Bot(command_prefix = "?")

#onready
@client.event
async def on_ready():
  print(f"{client.user} is ready to go, using OpenCord as the base")

#remove the help command
client.remove_command('help')

#ping
@client.command()
async def ping(ctx):
  await ctx.reply(f"Pong! in {round(client.latency * 1000)}ms")
  
#help
@client.command()
async def help(ctx):
  embed=nextcord.Embed(title="OpenCord Help", description="Here is a full list of all the commands", color=color)
  embed.add_field(name="----------------------------------------------------------------------------------------", value="Commands that require no permissions", inline=False)
  embed.add_field(name="ping", value="?ping, this command was made to see if the bot is working and alternatively viewing the api response latency of the client.", inline=False)
  embed.add_field(name="8ball", value="?8ball, simple right just ask a question and get a random answer", inline=False)
  embed.add_field(name="----------------------------------------------------------------------------------------", value="Commands that require permissions such as administrator", inline=True)
  embed.add_field(name="kick", value="?kick @user reason, to kick a user from the server", inline=False)
  embed.add_field(name="ban", value="?ban @user reason, to ban a user from the server", inline=False)
  await ctx.send(embed=embed)

#8ball
#you can add your own answers to the "responses" for example ["myresponse1", "myresponse2"]
@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
  responses = ["Maybe", "Absolutely", "I am certain", "Nope", "Not really no", "I can neither deny or confirm"]
  embed=nextcord.Embed(title="OpenCord has spoken!", description="100% Real answers, never wrong", color=color)
  embed.add_field(name="Question", value=f"{question}", inline=False)
  embed.add_field(name="Answer", value=f"{random.choice(responses)}", inline=True)
  await ctx.send(embed=embed)

#ban  
@client.command()
@has_permissions(ban_members = True)
async def ban(ctx, member : nextcord.Member, *, reason=None):
  embed=nextcord.Embed(title="Member has been banned", description="Here are the information about the event that happened", color=color)
  embed.add_field(name="Who banned the user?", value=f"{ctx.author.mention}", inline=False)
  embed.add_field(name="Who was banned?", value=f"{member.mention}", inline=True)
  embed.add_field(name="Reason", value=f"{reason}", inline=False)
  embed.set_footer(text="Aw man i kinda miss him")
  await ctx.send(embed=embed)
  await member.ban(reason=reason)

#kick
@client.command()
@has_permissions(kick_members = True)
async def kick(ctx, member : nextcord.Member, *, reason=None):
  embed=nextcord.Embed(title="Member has been kicked", description="Here are the information about the event that happened", color=color)
  embed.add_field(name="Who kicked the user?", value=f"{ctx.author.mention}", inline=False)
  embed.add_field(name="Who was kicked?", value=f"{member.mention}", inline=True)
  embed.add_field(name="Reason", value=f"{reason}", inline=False)
  embed.set_footer(text="Aw man i kinda miss him")
  await ctx.send(embed=embed)
  await member.kick(reason=reason)

#running the bot
client.run(os.environ["YourOwnTokenHere"])