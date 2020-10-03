import discord
from discord.ext import commands

token = os.environ.get("bot_token")
client = commands.Bot(command_prefix = 'tsj')

@client.event
async def on_ready():
    print("Bot is alive!")

client.run(token)