import discord,json,os
from discord.ext import commands
from discord.commands import Option
from discord.commands import slash_command

class create(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    create = discord.SlashCommandGroup(
        "create",
        "批量創建",
        guild_only=True,
        default_member_permissions=discord.Permissions(8),
    )

    @create.command(description="批量創建頻道")
    async def tchannel(self,ctx,
                       names:Option(str,"輸入用,隔開的多項字串"),
                       category:Option(discord.CategoryChannel,"創建至的類別")):
        await ctx.defer()
        try:
            names = names.split(",")
        except:
            await ctx.respond("請輸入正確的串列")
        
        for name in names:
            await ctx.guild.create_text_channel(name,category=category)

        await ctx.respond("創建完畢")
        
    @create.command(description="批量創建身份組")
    async def role(self,ctx,
                       names:Option(str,"輸入用,隔開的多項字串")):
        await ctx.defer()
        try:
            names = names.split(",")
        except:
            await ctx.respond("請輸入正確的串列")
        
        for name in names:
            await ctx.guild.create_role(name=name)

        await ctx.respond("創建完畢")

def setup (bot):
    bot.add_cog(create(bot))