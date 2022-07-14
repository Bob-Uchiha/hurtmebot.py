import discord
from discord.ext import commands

class Manager(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def bred(self,ctx):
        await ctx.send('cheese')
    @commands.command()
    async def kick(self,ctx,member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
    @commands.command()
    async def ban(self,ctx,member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
    @commands.command()
    async def unban(self,ctx,*,member):
        banned_users = await ctx.guild.bans()
        member_name,member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned{user.mention}')
def setup(client):
    client.add_cog(Manager(client))

