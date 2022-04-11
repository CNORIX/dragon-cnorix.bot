import discord
from discord.ext import commands
from discord import utils
from discord import channel
from discord.ext.commands.core import has_permissions
from discord.utils import get
from discord_components import DiscordComponents, Button, ButtonStyle

from itertools import chain
import asyncio
import requests
import json
import uuid
import datetime
import time
import os
import random

bot_prefix = 'dc/'
bot_token = 'OTA4NzQ2NzUyNDYxNTIwOTU3.YY6OXQ.iatjQBRew1h31anFSqUyJBt-A8s'

bot = commands.Bot(command_prefix = f'{ bot_prefix }', intents=discord.Intents.all())
DiscordComponents(bot)

alwaysOnline = 'No'
footertext = 'DragonBot By DragonFire. Powered by Python'
loadingEmoji = f'<a:loadingWin10db:823840940837437460>'

# Events

@bot.event
async def on_ready():
	print('Bot Connected!')
	await bot.change_presence(status=discord.Status.idle, activity=discord.Game(f"{bot_prefix}help | I'm on {len(bot.guilds)} servers"))

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

@bot.command()
async def about_dc(ctx):
	embed = discord.Embed(color = 0xff9900, title = 'DragonCloud - What is that')
	embed.add_field(name=f'DragonCloud is new cloud platform for everyone', value=f"It's save cloud platform for everyone and it's FREE", inline=False)
	embed.add_field(name=f'DragonCloud supports next languages:', value=f"PHP, CSS, JS, HTML. (More languages added soon)", inline=False)
	embed.add_field(name=f'Path to file example?', value=f"Path/To/File.php", inline=False)
	embed.set_footer(text=f'{ footertext }')
	await ctx.send(embed = embed)

@bot.command()
async def make_project(ctx, projectName, projectDescription):
	makingProject_msg = discord.Embed(
		title = f'Making project {loadingEmoji}',
		description = f'Please wait...',
		colour = discord.Colour.from_rgb(255, 0, 0)
	)
	await ctx.send(embed=makingProject_msg)

	os.system(f'mkdir projects\\{ctx.author.id}.proj')
	data = {
		"username": f"{ctx.author.name}",
		"discriminator": f"{ctx.author.discriminator}",
		"userid": f"{ctx.author.id}",
		"projectName": f"{projectName}",
		"projectDescription": f"{projectDescription}"
	}
	with open(f'projects\\{ctx.author.id}.proj\\{projectName}.json', 'w') as outfile:
		json.dump(data, outfile)

	with open(f'projects\\{ctx.author.id}.proj\\.htaccess', 'w') as htaccess:
		htaccess.write('ErrorDocument 404  "Error 404: Not found"\nErrorDocument 403 "Error 403: Access denied"\nErrorDocument 403 "Error 401: Unauthorized"')
		htaccess.close()

	makingProjectReady_msg = discord.Embed(
		title = f'Project created!',
		description = f'Thank you for creating project!',
		colour = discord.Colour.from_rgb(255, 0, 0)
	)
	await ctx.send(embed=makingProjectReady_msg)

@bot.command()
async def sendFileToProject(ctx):
	files = []
	for attachment in ctx.message.attachments:
		await attachment.save(f'projects\\{ctx.author.id}.proj\\{attachment.filename}')

	embed = discord.Embed(color = discord.Colour.from_rgb(156, 0, 0), title = 'File Uploaded Sucessfully!')
	embed.set_footer(text=f'{ footertext }')
	await ctx.send(embed = embed)

@bot.command()
async def run_code(ctx, pathToFile):
	try:
		youServerURL = f'http://{ctx.author.id}.proj/{pathToFile}'

		getURL = requests.get(youServerURL)
		embed = discord.Embed(color = discord.Colour.from_rgb(156, 0, 0), title = 'Requests GET')
		embed.add_field(name=f'Response code', value=f'```{ getURL }```', inline=False)
		embed.add_field(name=f'HTML Page Parse', value=f'```{ getURL.text }```', inline=False)
		embed.set_footer(text=f'{ footertext }')
		await ctx.send(embed = embed)

		postURL = requests.post(youServerURL)
		embed = discord.Embed(color = discord.Colour.from_rgb(156, 0, 0), title = 'Requests POST')
		embed.add_field(name=f'Response code', value=f'```{ postURL }```', inline=False)
		embed.add_field(name=f'HTML Page Parse', value=f'```{ postURL.text }```', inline=False)
		embed.set_footer(text=f'{ footertext }')
		await ctx.send(embed = embed)
	except requests.exceptions.ConnectionError:
		run_code_error = discord.Embed(
			title = f'Error occurred',
			description = f'Server is not available',
			colour = discord.Colour.from_rgb(255, 0, 0)
		)
		await ctx.send(embed=run_code_error)

bot.run(bot_token)