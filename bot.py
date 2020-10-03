import discord
from discord.ext import commands


client = commands.Bot(command_prefix = 'tsj')

@client.event
async def on_ready():
    print("Bot is alive!")

client.run(bot_token)