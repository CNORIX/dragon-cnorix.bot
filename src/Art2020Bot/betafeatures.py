import discord
from discord import *
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix="ab/", intents = discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence( status = discord.Status.idle, activity = discord.Game('ab/'))
    print(f'Bot: {bot.user.name} started!')

@bot.event
async def on_message(message):
    if message.author.bot: 
        return
    else:
        await message.delete()
        await message.channel.send(f'{message.author}: {message.content}')

@bot.event
async def on_command_error(ctx, error):
    embederror = discord.Embed(
        title = f'Ошибка',
        description = f'Во время выполнения кода произошла ошибка. Информация о ошибке: { error }. Ошибка уже была отправлена и скоро будет решена...',
        colour = discord.Colour.from_rgb(255, 0, 0)
    )
    await ctx.send(embed=embederror)

    report_errror_channel = bot.get_channel(874570653112606753)
    await report_errror_channel.send(error)

# ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}ms'.format(round(bot.latency, 1)))

bot.run("ODgyMTc1NjA2NjY0NjA5ODEy.YS3kDg.7IDBfHfKkIc4azdXouFtYfPZvr0")
