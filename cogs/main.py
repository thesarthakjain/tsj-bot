import discord
from discord.ext import commands
import os
import random
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
        await ctx.send(f'***TSJ version: 1.34***')
        print("version command used")

    @commands.command(aliases = ['com','commands'])
    async def _commands(self, ctx):
        await ctx.send(f'**Some commands for <@761623837263265803> are:**' \
           '```com/commands(obviously) \nintro \nclear <number of messages> \ngit/github \nping'\
        '\n8ball <Your question> \nkick <member tag> <reason(optional)> \nban <member tag> <reason(optional)>'\
        '\nunban <name>#<discriminator>```')
        print("commands command used")

    @commands.command()
    async def intro(self, ctx):
        await ctx.send(f"*Hello, I am <@761623837263265803> discord bot.\n" \
                        "My father's name is <@629276069878562817>.**")
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
        await ctx.send(f'***https://github.com/thesarthakjain/tsj-bot***')
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
        responses = ['As I see it, yes.',
             'Ask again later.',
             'Better not tell you now.',
             'Cannot predict now.',
             'Concentrate and ask again.',
             'Don’t count on it.',
             'It is certain.',
             'It is decidedly so.',
             'Most likely.',
             'My reply is no.',
             'My sources say no.',
             'Outlook not so good.',
             'Outlook good.',
             'Reply hazy, try again.',
             'Signs point to yes.',
             'Very doubtful.',
             'Without a doubt.',
             'Yes.',
             'Yes – definitely.',
             'You may rely on it.']
        await ctx.send(f'**Question: {question}\nAnswer: {random.choice(responses)}**')
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