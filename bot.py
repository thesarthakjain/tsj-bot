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

@client.command(aliases = ['ver'])
async def version(ctx):
    await ctx.send(f'***TSJ version: {com.version}***')
    print("version command used")

@client.command(aliases = ['com'])
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
    await ctx.send(f'**Pong bolu kya? :rofl:**')
    await ctx.send(f'**{round(client.latency*1000)} ms, khush?**')
    print('ping command used.')

@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question):
    await ctx.send(f'**Question: {question}\nAnswer: {random.choice(com._8ball)}**')
    print('8ball command used.')


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):    
    await member.kick(reason = reason)
    await ctx.send(f'**{member.name}#{member.discriminator} has been kicked.**')
    print(f'{member.name}#{member.discriminator} has been kicked from a server because {reason}.')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason = reason)
    await ctx.send(f'**{member.name}#{member.discriminator} has been banned.**')
    print(f'{member.name}#{member.discriminator} has been banned from a server for the reason: {reason}.')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'**{user.name}#{user.discriminator} has been unbanned.**')
            print(f'{user.name}#{user.discriminator} has been unbanned from a server.')
            return
    await ctx.send(f'**{member_name}#{member_discriminator} not found in server ban list.**')

client.run(token)
