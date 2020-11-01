#for sensitive system commands

import discord
from discord.ext import commands
import os
import platform
import asyncio

class main(commands.Cog):
    def __init__(self,client):
        self.client = client

    def is_owner():
        async def predicate(ctx):
            return ctx.author.id == 629276069878562817 #my discord id
        return commands.check(predicate)

    @commands.command()
    @is_owner()
    async def reboot(self, ctx):
        await ctx.send('Do you wanna continue? (Y/N)')
        try:
            msg = await self.client.wait_for('message', timeout = 5)
            if msg.content == 'y' or msg.content == 'Y':
                
                await ctx.send('Rebooting the system.')
                print('rebooting the system')
                if platform.platform()[0:7] == "Windows":
                    os.system("shutdown /r")
                elif platform.platform()[0:5] == "Linux":
                    os.system("sudo reboot")
                else :
                    print("OS not supported.")
        except asyncio.TimeoutError:
            await ctx.send('You took too long...')
            print('took too long to use reboot command.')

        
    @commands.command()
    @is_owner()
    async def shutdown(self, ctx):
        await ctx.send('Do you wanna continue? (Y/N)')
        try:
            msg = await self.client.wait_for('message', timeout = 5)
            if msg.content == 'y' or msg.content == 'Y':
                
                await ctx.send('Turing the system off.')
                print('turning the system off')
                if platform.platform()[0:7] == "Windows":
                    os.system("shutdown /s")
                elif platform.platform()[0:5] == "Linux":
                    os.system("sudo poweroff")
                else :
                    print("OS not supported.")
        except asyncio.TimeoutError:
            await ctx.send('You took too long...')
            print('took too long to use the shutdown command')


    @commands.command()
    @is_owner()
    async def cls(self, ctx):
        await ctx.send('Do you wanna continue? (Y/N)')
        try:
            msg = await self.client.wait_for('message', timeout = 5)
            if msg.content == 'y' or msg.content == 'Y':    
                await ctx.send('Clearing the logs.')
                print('clearing the logs')
                if platform.platform()[0:7] == "Windows":
                    os.system("cls")                    
                    print('logs cleared')
                    await ctx.send('Logs cleared')
                elif platform.platform()[0:5] == "Linux":
                    os.system("cls")
                    print('logs cleared')
                    await ctx.send('Logs cleared')
                else :
                    print("OS not supported")
                    await ctx.send('OS not supported.')
        except asyncio.TimeoutError:
            await ctx.send('You took too long...')
            print('took too long to use cls command.')



def setup(client):
    client.add_cog(main(client))