#for moderation commands

admin_role = "admin" #role that can use kick, ban and unban

import discord
from discord.ext import commands
import os
import random
import time

class main(commands.Cog):
    def __init__(self,client):
        self.client = client


    @commands.command()
    @commands.has_role(admin_role)
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
            await ctx.send('**Please tag the account.**')
            print("no arguement was given  in kick command")
        else:
            await ctx.send(f"**You do not have {admin_role} role to use that command.**")
            print("no permission to kick")


    @commands.command()
    @commands.has_role(admin_role)
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
            await ctx.send('**Please tag the account.**')
            print("no arguement was given  in ban command")
        else:
            await ctx.send(f"**You do not have {admin_role} role to use that command.**")
            print("no permission to ban")


    @commands.command()
    @commands.has_role(admin_role)
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
            await ctx.send('**Please add the name and discriminator.**')
            print("no arguement was given  in unban command")
        else:
            await ctx.send(f"**You do not have {admin_role} role to use that command.**")
            print("no permission to unban")



def setup(client):
    client.add_cog(main(client))