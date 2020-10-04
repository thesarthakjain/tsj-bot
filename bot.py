import discord
from discord.ext import commands
import os

token = os.environ.get('bot_token')
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)


#events
@client.event
async def on_ready():
    print('Bot is working :)')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')


#commands
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong bolu kya? :rofl:')
    await ctx.send(f'{round(client.latency*1000)} ms')


client.run(token)
