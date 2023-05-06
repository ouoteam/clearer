import discord
from discord.commands import Option
from discord.ext import commands


class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    delete = discord.SlashCommandGroup(
        "delete",
        "清理群組",
        guild_only=True,
        default_member_permissions=discord.Permissions(8),
    )

    @delete.command(description="刪除所有頻道")
    async def channel(self, ctx):
        await ctx.defer()
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except:
                continue

    @delete.command(description="刪除所有身分組")
    async def role(self, ctx):
        await ctx.defer()
        for role in ctx.guild.roles:
            try:
                await role.delete()
            except:
                continue

    @delete.command(description="刪除同一個名字的所有文字頻道")
    async def cname(self,ctx,name:Option(discord.TextChannel,"同一個名字的頻道？")):
        await ctx.defer()
        for channel in ctx.guild.channels:
            if channel.name == name.name:
                await channel.delete()

    @delete.command(description="刪除同一個名字的所有語音頻道")
    async def vname(self,ctx,name:Option(discord.VoiceChannel,"同一個名字的頻道？")):
        await ctx.defer()
        for channel in ctx.guild.channels:
            if channel.name == name.name:
                await channel.delete()

    @delete.command(description="刪除類別中的所有頻道")
    async def category(self,ctx,category:Option(discord.CategoryChannel,"要清空的類別")):
        await ctx.defer()
        for channel in ctx.guild.channels:
            if channel.category == category:
                await channel.delete()

def setup(bot):
    bot.add_cog(main(bot))
