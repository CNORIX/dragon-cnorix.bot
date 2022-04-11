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
async def on_command_error(ctx, error):
    embederror = discord.Embed(
        title = f'Ошибка',
        description = f'Во время выполнения кода произошла ошибка. Информация о ошибке: { error }. Ошибка уже была отправлена и скоро будет решена...',
        colour = discord.Colour.from_rgb(255, 0, 0)
    )
    await ctx.send(embed=embederror)

    report_errror_channel = bot.get_channel(874570653112606753)
    await report_errror_channel.send(error)

@bot.command()
async def say(ctx, *, msg):
    await ctx.send(msg)

@bot.command()
async def send_question(ctx, *, question):
    question_channel = bot.get_channel(847700531522043945)

    embedquestion = discord.Embed(
        title = f'{ctx.author.name}#{ctx.author.discriminator}',
        description = f'{question}',
        colour = discord.Colour.from_rgb(255, 0, 0)
    )
    await question_channel.send(embed=embedquestion)

    embedquestionsucess = discord.Embed(
        title = f'Получилось!',
        description = f'Ваш вопрос был отправлен',
        colour = discord.Colour.from_rgb(255, 0, 0)
    )
    await ctx.send(embed=embedquestionsucess)

@bot.command()
async def send_idea(ctx, *, question):
    question_channel = bot.get_channel(847700531258720315)

    embedquestion = discord.Embed(
        title = f'{ctx.author.name}#{ctx.author.discriminator}',
        description = f'{question}',
        colour = discord.Colour.from_rgb(255, 0, 0)
    )
    await question_channel.send(embed=embedquestion)

    embedquestionsucess = discord.Embed(
        title = f'Получилось!',
        description = f'Ваша идея был отправлена',
        colour = discord.Colour.from_rgb(255, 0, 0)
    )
    await ctx.send(embed=embedquestionsucess)

# ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}ms'.format(round(bot.latency, 1)))

bot.run("ODc0MzUxNjgzMjE4NTcxMzA1.YRFtdQ.UUAwqsJB1jnwBo7gOwfQf-Ce07U")
