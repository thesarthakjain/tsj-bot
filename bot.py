import discord
from discord.ext import commands
import cred


client = commands.Bot(command_prefix = 'tsj')

@client.event
async def on_ready():
    print("Bot is alive!")

client.run(cred.bot_token)