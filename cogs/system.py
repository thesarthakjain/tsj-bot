#for sensitive system commands

import discord
from discord.ext import commands
import os
import platform

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
        await ctx.send('Rebooting the system.')
        print('rebooting the system')
        if platform.platform()[0:7] == "Windows":
            os.system("shutdown /r")
        elif platform.platform()[0:5] == "Linux":
            os.system("sudo reboot")
        else :
            print("OS not supported.")

    @commands.command()
    @is_owner()
    async def shutdown(self, ctx):
        await ctx.send('Turning off the system.')
        print('turning off the system')
        if platform.platform()[0:7] == "Windows":
            os.system("shutdown /s")
        elif platform.platform()[0:5] == "Linux":
            os.system("sudo poweroff")
        else :
            print("OS not supported.")




def setup(client):
    client.add_cog(main(client))