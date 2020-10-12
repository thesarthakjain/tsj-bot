#for general purpose commands

manager_role = "manager" #role that can use clear and  spam commands

import discord
from discord.ext import commands
import os
import random
import time

class main(commands.Cog):
    def __init__(self,client):
        self.client = client


    @commands.command()
    @commands.has_role(manager_role)
    async def clear(self, ctx, amount = 1):
        await ctx.channel.purge(limit = amount+1)
        if amount == 1 :
            await ctx.send(f'`{amount} message cleared.`')
        else :
            await ctx.send(f'`{amount} messages cleared.`')
        time.sleep(1)
        await ctx.channel.purge(limit = 1)
        print(f'{amount} messages cleared.')
    @clear.error
    async def clear_error(self, ctx, error):
        await ctx.send(f'**You do not have {manager_role} role to use that command.**')
        print("no permission to use clear")

    
    @commands.command(aliases = ['8ball'])
    async def a8ball(self, ctx, *, question):
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
    @a8ball.error
    async def a8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Please add a question.**')
            print("no arguement was given  in 8ball command")


    @commands.command()
    @commands.has_role(manager_role)
    async def spam (self, ctx, delay, duration, msg = "ping"):
        if float(delay) < 2:
            await ctx.send("**Delay can not be lesser than 2 seconds.**")
            print("spam failed bec delay < 2 sec")
        elif float(duration) > 600:
            await ctx.send("**Duration can not exceed 600 seconds.**")
            print("spam failed bec duration > 600 sec")
        else:
            start = time.time()
            end = start
            while(True):
                if msg == "ping":
                    await ctx.send(f'**{round(self.client.latency*1000)} ms**')
                else:
                    await ctx.send(f'**{msg}**')
                time.sleep(float(delay))
                if end-start >= float(duration):
                    return
                end = time.time()
            print("spam command was used")
    @spam.error
    async def spam_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Please add delay, duration and message.**')
            print("no arguement was given  in spam command")
        else:
            await ctx.send(f'**You do not have {manager_role} role to use that command.**')
            print('no permission to use spam command')

    
def setup(client):
    client.add_cog(main(client))