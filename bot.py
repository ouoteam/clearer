import json
import discord

bot = discord.Bot(help_command=None, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f">>{bot.user}上線<<")
    game = discord.Game("ouoc | 程式同好群 | 自介加入")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command(description="感到臃腫？")
async def help(ctx):
    await ctx.defer()
    file = open("data/help.txt","r",encoding="utf-8")
    text = file.read()
    embed=discord.Embed(description=text,color=discord.Colour.random())
    embed.set_footer(text=F"{len(bot.guilds)}群 | {len(bot.users)}用戶")
    await ctx.respond(embed=embed)

if __name__ == "__main__":
    for key, value in bot.load_extension("cogs", recursive=True, store=True).items():
        if value == True:
            print(f"成功載入插件 {key}")
        else:
            print(f"載入插件 {key} 失敗: {value}")
    with open("data/config.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    bot.run(data["token"])