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
        await ctx.send(f'Kicked {member.mention}. Come back when you\'re ready to talk nice')
    @commands.command()
    async def ban(self,ctx,member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}. Get the hell out of here')

    @commands.command()
    async def unban(self,ctx,*,member):
        banned_users = await ctx.guild.bans()
        member_name,member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned{user.mention}. Welcome back to hell.')
def setup(client):
    client.add_cog(Manager(client))

