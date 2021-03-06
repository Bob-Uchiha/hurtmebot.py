import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import time
       

load_dotenv()
client = commands.Bot(command_prefix='n.', help_command=commands.MinimalHelpCommand())
TOKEN = os.getenv('TOKEN')
@client.command
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
@client.command
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
@client.command()
async def ping(ctx):
    await ctx.send(f'Your current latency is {round(client.latency * 1000)}ms')
@client.command()
async def clear(ctx, amount):
    if amount.lower() == 'all':
        await ctx.channel.purge(limit=1000000)
    else:
        await ctx.channel.purge(limit=int(amount)+1)



client.run(TOKEN)
