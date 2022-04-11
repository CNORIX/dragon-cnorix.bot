print('Loading...')

import discord
from discord.ext import commands
from discord import utils
from discord import channel
from discord.ext.commands.core import has_permissions
from discord.utils import get

import requests
import os

bot_prefix = 'dfc/'
bot_token = 'OTIyNzc0Nzc2MDE0MDY1Njg0.YcGW-g.i-0kIsllVup3QPgGmauI4Dw3SF0'

activity = discord.Streaming(name=f"{bot_prefix}help", url="https://www.twitch.tv/discord")
bot = commands.Bot(command_prefix = f'{ bot_prefix }', intents=discord.Intents.all(), help_command=None, activity=activity, status=discord.Status.idle)

alwaysOnline = 'No'
footertext = 'DragonFire Community Bot By DragonFire. Powered by Python'
loadingEmoji = f'<a:loadingWin10db:823840940837437460>'

# Events

@bot.event
async def on_ready():
	print('Bot Connected!')

@bot.event
async def on_closed():
	print('Bot Disconnected!')

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		embederror = discord.Embed(
			title = f'Error',
			description = f'This command is not found',
			colour = discord.Colour.from_rgb(255, 0, 0)
		)
		await ctx.send(embed=embederror)
		pass
	if isinstance(error, commands.CommandOnCooldown):
		embederror = discord.Embed(
			title = f'Error',
			description = f'This command is ratelimited, please try again in { error.retry_after }',
			colour = discord.Colour.from_rgb(255, 0, 0)
		)
		await ctx.send(embed=embederror)
		pass
	else:
		print(error)
		embederror = discord.Embed(
			title = f'Error',
			description = f'An error occurred while executing the code. Error information: ```{ error }``` The error has already been submitted and will be resolved soon...',
			colour = discord.Colour.from_rgb(255, 0, 0)
		)
		await ctx.send(embed=embederror)

		report_errror_channel = bot.get_channel(891568518632464384)
		await report_errror_channel.send(f'```{error}```')
		pass

@bot.event
async def on_button_click(interaction):
	if interaction.responded:
		return
	else:
		embederror = discord.Embed(
			title = f'Error',
			description = f'This interaction is not available. Please execute this command again',
			colour = discord.Colour.from_rgb(255, 0, 0)
		)
		await interaction.send(embed=embederror)

# Help Command
@bot.command()
async def help(ctx):
	embed = discord.Embed(color = discord.Colour.from_rgb(156, 0, 0), title = 'Help')
	embed.add_field(name=f'{ bot_prefix }none', value=f"None", inline=True)
	embed.add_field(name=f'{ bot_prefix }none', value=f"None", inline=True)
	embed.set_footer(text=f'{ footertext }')
	await ctx.send(embed = embed)

@bot.command()
async def ping(ctx):
    await ctx.send(f'My ping is {bot.latency * 1000}')

@bot.command()
@commands.is_owner()
async def welcome(ctx):
	embed = discord.Embed(color = discord.Colour.from_rgb(156, 0, 0), title = 'DragonFire Community Welcome')
	embed.add_field(name=f'Russian', value=f"Здраствуй, друг,\nДобро пожаловать на официальный дискорд сервер DragonFireа.\nПеред общением пожалуйста прочитай правила ниже\nЕсли вам трудно перемещаться между правилами, мы прикрепили логотип каждой категорий\nСсылка приглашение: https://discord.gg/NgphMgmVPU", inline=False)
	embed.add_field(name=f'English', value=f"Hello, friend,\nWelcome to the official DragonFire discord server.\nBefore you chat, please read the rules below.\nIf you find it hard to navigate between the rules, we have attached a logo to each category\nInvitation link: https://discord.gg/NgphMgmVPU", inline=False)
	embed.set_footer(text=f'{ footertext }')
	await ctx.send(embed = embed)

@bot.command()
@commands.is_owner()
async def rules(ctx):
	embed = discord.Embed(color = discord.Colour.from_rgb(156, 0, 0), title = 'DragonFire Community Rules')
	embed.add_field(name=f'Russian', value=f"Правила перемещены на вебсайт\nСсылка: http://dragonfirecommunity.7m.pl/rules/rules-ru.html", inline=False)
	embed.add_field(name=f'English', value=f"Rules moved to the website\nLink: http://dragonfirecommunity.7m.pl/rules/rules-en.html", inline=False)
	embed.set_footer(text=f'{ footertext }')
	await ctx.send(embed = embed)

@bot.command()
@commands.is_owner()
async def servers(ctx):
	embed = discord.Embed(color = discord.Colour.from_rgb(156, 0, 0), title = 'DragonFire Community Servers')
	embed.add_field(name=f'DragonCraft', value=f"Only hamachi", inline=False)
	embed.set_footer(text=f'{ footertext }')
	await ctx.send(embed = embed)

@bot.command()
@commands.is_owner()
async def services(ctx):
	embed = discord.Embed(color = discord.Colour.from_rgb(156, 0, 0), title = 'DragonFire Community Services')
	embed.add_field(name=f'Services', value=f"My services:\n - **H**elp you with DragonPS: *Not available because server is not available*\n - **H**elp you with DragonCoreGD: **Free**\n - **B**eta testing: `Only for mods`\n - **C**reate **D**iscord **B**ot: Not available\n - **D**ragon**S**tore: **Free** URL: http://dragonstore.7m.pl/\n - **M**y **S**ite: **Free** URL: http://dragonfire.7m.pl/", inline=False)
	embed.set_footer(text=f'{ footertext }')
	await ctx.send(embed = embed)

@bot.command()
@commands.is_owner()
async def status_pages(ctx):
	embed = discord.Embed(color = discord.Colour.from_rgb(156, 0, 0), title = 'DragonFire Community Status Pages')
	embed.add_field(name=f'Status Pages', value=f"**S**tatus pages:\n - **S**ervers: https://stats.uptimerobot.com/q6EDys1XYQ\n - **B**ots:\n   - **D**ragon**B**ot: https://status.watchbot.app/bot/852183551075811368\n   - **D**ragon**C**loud: https://status.watchbot.app/bot/908746752461520957\n- **C**ompact statuspage: https://dragonfire1.statuspage.io/", inline=False)
	embed.set_footer(text=f'{ footertext }')
	await ctx.send(embed = embed)

bot.run(bot_token)