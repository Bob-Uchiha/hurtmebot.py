import discord 
from discord.ext import commands
from random import *
import time
class Tools(commands.Cog):
    def __init__ (self,client):
        self.client = client
    @commands.command(aliases=['dice'])
    async def die(self,ctx,x=6):
        response = (f'{randrange(1,x + 1)}')
        await ctx.send(response)
    @commands.command(description='funny dream song')
    async def dream(self,ctx):
        print('reading')
        with open('cogs/dream.txt', 'r') as f:
            song = [line.strip() for line in f]
        for i in song:
            await ctx.send(i)
            time.sleep(2)
    @commands.command(aliases=['pvp','versus'])
    async def fight(self,ctx,x,y):
        await ctx.send(f'aight so {x} will fight {y}')
        seed = random()
        if seed < 0.5:
            await ctx.send(f'{x} has won')
        elif seed > 0.5:
            await ctx.send(f'{y} has won')
        elif seed == 0.5:
            await ctx.send('Your blades collide with force, and break instantly. You idiots shouldn\'t have bought those pieces of crap from the flea market.')
        
def setup(client):
    client.add_cog(Tools(client))
