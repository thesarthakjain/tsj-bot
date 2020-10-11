#for bot info/functioning
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
        await self.client.change_presence(activity=discord.Game("with my feelings."))
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
        await ctx.send(f'***TSJ version: 1.39***')
        print("version command used")


    @commands.command(aliases = ['com','commands'])
    async def _commands(self, ctx):
        await ctx.send(f'**Some commands for <@761623837263265803> are:**' \
           '```com/commands(obviously) \nintro \nclear <number of messages> \ngit/github \nping'\
        '\n8ball <Your question> \nkick <member tag> <reason(optional)> \nban <member tag> <reason(optional)>'\
        '\nunban <name>#<discriminator> \nspam <delay> <duration> <spam message/ping>```')
        print("commands command used")


    @commands.command()
    async def intro(self, ctx):
        await ctx.send(f"**Hello, I am <@761623837263265803> discord bot.\n" \
                        "My father's name is <@629276069878562817>.**")
        print("intro command used")


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

    
def setup(client):
    client.add_cog(main(client))