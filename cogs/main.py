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
        await ctx.send(f'***TSJ version: 1.38***')
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
            await ctx.send('Please add a question.')
            print("no arguement was given  in 8ball command")


    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):    
        try:
            await member.kick(reason = reason)
            await ctx.send(f'**{member.name}#{member.discriminator} has been kicked.**')
            print(f'{member.name}#{member.discriminator} has been kicked from a server because {reason}.')
        except:
            await ctx.send(f'**{member.name}#{member.discriminator} can not be kicked.**')
            print(f'{member.name}#{member.discriminator} can not be kicked from a server.')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please tag the account.')
            print("no arguement was given  in kick command")

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        try:
            await member.ban(reason = reason)
            await ctx.send(f'**{member.name}#{member.discriminator} has been banned.**')
            print(f'{member.name}#{member.discriminator} has been banned from a server for the reason: {reason}.')
        except:
            await ctx.send(f'**{member.name}#{member.discriminator} can not be banned.**')
            print(f'{member.name}#{member.discriminator} can not be banned from a server.')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please tag the account.')
            print("no arguement was given  in ban command")

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

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please add the name and discriminator.')
            print("no arguement was given  in unban command")

    @commands.command()
    async def spam (self, ctx, delay, duration, msg = "ping"):
        if float(delay) < 2:
            await ctx.send("Delay can not be lesser than 2 seconds.")
            print("spam failed bec delay < 2 sec")
        elif float(duration) > 600:
            await ctx.send("Duration can not exceed 600 seconds.")
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
            await ctx.send('Please add delay, duration and message.')
            print("no arguement was given  in spam command")

def setup(client):
    client.add_cog(main(client))