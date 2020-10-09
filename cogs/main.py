import discord
from discord.ext import commands
import os
import random
import com
import time

class main(commands.Cog):
    def __init__(self,client):
        self.client = client


#events
    @commands.Cog.listener()
    async def on_ready(self):
        print('bot is online!')

    @commands.Cog.listener()
    async def on_member_join(self,member):
        print(f'{member} has joined a server.')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print(f'{member} has left a server.')



#commands
    @commands.command(aliases = ['ver'])
    async def version(self, ctx):
        await ctx.send(f'***TSJ version: {com.version}***')
        print("version command used")

    @commands.command(aliases = ['com','commands'])
    async def _commands(self, ctx):
        await ctx.send(f'{com.commands}')
        print("commands command used")

    @commands.command()
    async def intro(self, ctx):
        await ctx.send(f'{com.intro}')
        print("intro command used")

    @commands.command()
    async def clear(self, ctx, amount = 1):
        await ctx.channel.purge(limit = amount+1)
    
        if amount == 1 :
            await ctx.send(f'`{amount} message cleared.`')
        else :
            await ctx.send(f'`{amount} messages cleared.`')
    
        time.sleep(1)
        await ctx.channel.purge(limit = 1)
        print(f'{amount} messages cleared.')

    @commands.command(aliases = ['git'])
    async def github(self, ctx):
        await ctx.send(f'{com.github}')
        print("github command used")

    @commands.command()
    async def ping(self, ctx):
        num = random.randint(0,9)
        if num == 0:
            await ctx.send(f'**Pong bolu kya? :rofl:**')
            await ctx.send(f'**{round(self.client.latency*1000)} ms, khush?**')
        else:
            await ctx.send(f'**{round(self.client.latency*1000)} ms**')
        print('ping command used.')

    @commands.command(aliases = ['8ball'])
    async def _8ball(self, ctx, *, question):
        await ctx.send(f'**Question: {question}\nAnswer: {random.choice(com._8ball)}**')
        print('8ball command used.')


    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):    
        await member.kick(reason = reason)
        await ctx.send(f'**{member.name}#{member.discriminator} has been kicked.**')
        print(f'{member.name}#{member.discriminator} has been kicked from a server because {reason}.')

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason = reason)
        await ctx.send(f'**{member.name}#{member.discriminator} has been banned.**')
        print(f'{member.name}#{member.discriminator} has been banned from a server for the reason: {reason}.')

    @commands.command()
    async def unban(self, ctx, *, member):
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


def setup(client):
    client.add_cog(main(client))