import discord 
from discord.ext import commands
import random
import time
class Tools(commands.Cog):
    def __init__ (self,client):
        self.client = client
    @commands.command(aliases=['dice'])
    async def die(self,ctx,x=6):
        response = (f'{random.randrange(1,x)}')
        await ctx.send(response)
    @commands.command()
    async def dream(self,ctx):
        print('reading')
        with open('cogs/dream.txt', 'r') as f:
            song = [line.strip() for line in f]
        for i in song:
            await ctx.send(i)
            time.sleep(2)
def setup(client):
    client.add_cog(Tools(client))
