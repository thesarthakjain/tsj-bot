import discord
from discord.ext import commands
import os
import random
import com
import time

token = os.environ.get('bot_token')
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)


#events
@client.event
async def on_ready():
    print('bot is online and working!')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')


#commands
@client.command()
async def commands(ctx):
    await ctx.send(f'{com.commands}')
    print("commands command used")

@client.command()
async def intro(ctx):
    await ctx.send(f'{com.intro}')
    print("intro command used")

@client.command()
async def clear(ctx, amount = 1):
    await ctx.channel.purge(limit = amount+1)
    
    if amount == 1 :
        await ctx.send(f'`{amount} message cleared.`')
    else :
        await ctx.send(f'`{amount} messages cleared.`')
    
    time.sleep(1)
    await ctx.channel.purge(limit = 1)
    print(f'{amount} messages cleared.')

@client.command(aliases = ['git'])
async def github(ctx):
    await ctx.send(f'{com.github}')
    print("github command used")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong bolu kya? :rofl:')
    await ctx.send(f'{round(client.latency*1000)} ms, khush?')
    print('ping command used.')

@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question):
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(com._8ball)}')
    print('8ball command used.')


client.run(token)
