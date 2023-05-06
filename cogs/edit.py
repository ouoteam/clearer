import discord,json,os
from discord.ext import commands
from discord.commands import Option
from discord.commands import slash_command

class edit(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    edit = discord.SlashCommandGroup(
        "edit",
        "編輯群組",
        guild_only=True,
        default_member_permissions=discord.Permissions(8),
    )    

    @edit.command(description="為所有頻道新增前綴")
    async def aprefix(self,ctx,pr:Option(str,"前綴符號")):
        await ctx.defer()
        for channel in ctx.guild.channels:
            try:
                await channel.edit(name=F"{pr}{channel.name}")
            except:
                continue
        await ctx.respond("已更改所有頻道前綴")

    @edit.command(description="為所有頻道移除前綴")
    async def dprefix(self,ctx,pr:Option(str,"前綴符號")):
        await ctx.defer()
        for channel in ctx.guild.channels:
            try:
                name = channel.name.replace(pr,"")
                await channel.edit(name=name)
            except:
                continue
        await ctx.respond("已更改所有頻道前綴")

def setup (bot):
    bot.add_cog(edit(bot))