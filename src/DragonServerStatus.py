import discord
from discord import *
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix="dss/", intents = discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence( status = discord.Status.idle, activity = discord.Game('Bot started'))
    print(f'Bot: {bot.user.name} connected!')

@bot.command()
async def status(ctx):
    sql_status_url = 'http://dragonfire.7m.pl/api/checkSqlStatus.php'
    webserver_status_url = 'http://dragonfire.7m.pl/api/checkWebServer.php'

    sql_status_check = requests.get(sql_status_url)
    webserver_status_check = requests.get(webserver_status_url)

    embed = discord.Embed(
        title = 'DragonFire servers status',
        description = f'SQL Status (dragonfire.7m.pl): { sql_status_check.status_code }\n Webserver status (dragonfire.7m.pl): { webserver_status_check.status_code }',
        colour = discord.Colour.from_rgb(139, 0, 0)
    )
    await ctx.send(embed=embed)
    
bot.run(f'ODg4Nzg4MjE2MTg5MTY1NjIw.YUXyhw.IIjh08UbkqfOYc31C_ZXlys0J2k')
