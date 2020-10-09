import discord
from discord.ext import commands
import os
import random
import com
import time

token = os.environ.get('bot_token')
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension}') 
    print(f'loaded {extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension}')
    print(f'unloaded {extension}')

@client.command()
async def reload(ctx, extension = "all"):
    if extension == "all":
        for file_name in os.listdir('./cogs'):
            if file_name.endswith('.py'):
                client.unload_extension(f'cogs.{file_name[:-3]}')
                client.load_extension(f'cogs.{file_name[:-3]}')
        await ctx.send(f'Reloaded {extension}')
        print(f'reloaded {extension}')

    else:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'Reloaded {extension}')
        print(f'reloaded {extension}')

for file_name in os.listdir('./cogs'):
    if file_name.endswith('.py'):
        client.load_extension(f'cogs.{file_name[:-3]}')

client.run(token)