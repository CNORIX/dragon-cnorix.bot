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
import datetime
import time
import os
import random
from PIL import Image, ImageDraw, ImageFont
import sys

bot_prefix = 'db/'
bot_token = 'ODUyMTgzNTUxMDc1ODExMzY4.YMDHxw.1Eap4fBut9EBIjBwpxLqtinS34k'

bad_words = ["bitch", "poop", "dump", "stupid", "тупой", "глупый", "говно", "сука", "пиздец", "хуй", "нахуй", "похуй"]
hi_words = ["hi", "hello"]
how_are_you_words = ["how are you?", "how is it going?"]

bot = commands.Bot(command_prefix = f'{ bot_prefix }', intents=discord.Intents.all())
DiscordComponents(bot)

alwaysOnline = 'No'
footertext = 'DragonBot By DragonFire. Powered by Python'
loadingEmoji = f'<a:loadingWin10db:823840940837437460>'

# Events

@bot.event
async def on_ready():
	print('Bot Connected!')
	await bot.change_presence(status=discord.Status.idle, activity=discord.Game(f"{bot_prefix}help"))

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
async def on_message( message ):
	try:
		GuildImg = Image.open("GuildImg.png")
	except:
		print("Unable to load image")

	idraw = ImageDraw.Draw(GuildImg)
	text = f"DragonFire\nMembers:\n{message.guild.member_count}"

	font = ImageFont.truetype("arial.ttf", size=18)

	idraw.text((0, 0), text, (255,255,255),font=font)

	GuildImg.save('GuildImg.png')

	with open('GuildImg.png', 'rb') as GuildImgNew:
		icon = GuildImgNew.read()

	await message.guild.edit(icon=icon)



	await bot.process_commands( message )

	msg = message.content.lower()

	if msg in bad_words:
		await message.delete()
		await message.author.send(f"{ message.author.name }, Please don't write bad words!")

	if msg in hi_words:
		if message.author.id == bot.user.id:
			pass
		else:
			await message.channel.send(f'Hello!')

	if msg in how_are_you_words:
		if message.author.id == bot.user.id:
			pass
		else:
			await message.channel.send(f"I'm fine. How about you?")

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

@bot.event
async def on_member_join( member ):
	embed_join_error = discord.Embed(
		title = f'Error',
		description = f'Hello, {member.name}! You are trying to join {member.guild}. This server is NOT avialable. Sorry...',
		colour = discord.Colour.from_rgb(255, 0, 0)
	)
	await member.send(embed=embed_join_error)
	await member.kick()

# Animals images

@bot.command(brief = 'Animals')
async def animals(ctx):
	await ctx.send("Animals",
		components = [
			Button(label = "Panda", custom_id = "Panda"),
			Button(label = "Dog", custom_id = "Dog"),
			Button(label = "Cat", custom_id = "Cat"),
			Button(label = "Fox", custom_id = "Fox") 
		]
	)
	interaction = await bot.wait_for("button_click")
	
	if interaction.custom_id == 'Panda':
		response = requests.get('https://some-random-api.ml/img/panda')
		json_data = json.loads(response.text)

		embed = discord.Embed(color = 0xff9900, title = 'Random Panda')
		embed.set_image(url = json_data['link'])
		embed.set_footer(text=f'{ footertext }')
		await interaction.respond(embed = embed)
	if interaction.custom_id == 'Dog':
		response = requests.get('https://some-random-api.ml/img/dog')
		json_data = json.loads(response.text)

		embed = discord.Embed(color = 0xff9900, title = 'Random Dog')
		embed.set_image(url = json_data['link'])
		embed.set_footer(text=f'{ footertext }')
		await interaction.respond(embed = embed)
	if interaction.custom_id == 'Cat':
		response = requests.get('https://some-random-api.ml/img/cat')
		json_data = json.loads(response.text)

		embed = discord.Embed(color = 0xff9900, title = 'Random Cat')
		embed.set_image(url = json_data['link'])
		embed.set_footer(text=f'{ footertext }')
		await interaction.respond(embed = embed)
	if interaction.custom_id == 'Fox':
		response = requests.get('https://some-random-api.ml/img/fox')
		json_data = json.loads(response.text)
	
		embed = discord.Embed(color = 0xff9900, title = 'Random Fox')
		embed.set_image(url = json_data['link'])
		embed.set_footer(text=f'{ footertext }')
		await interaction.respond(embed = embed)

# Moderator commands

@bot.command(brief = 'Ban user from guild')
@commands.has_permissions(ban_members = True)
async def mod_ban(ctx, member : discord.Member, *, reason = None):
	await member.ban(reason = reason)
	embed = discord.Embed(color = 0xff9900, title = 'Ban')
	embed.add_field(name=f'User *{ member }* banned from this server successfully. ', value=f'Reason: { reason }', inline=False)
	embed.set_footer(text=f'{ footertext }')
	await ctx.send(embed = embed)

@bot.command( brief = 'Kick user from guild')
@commands.has_permissions(kick_members=True)
async def mod_kick(ctx, user: discord.Member, *, reason = None):
	if not reason:
		await user.kick()
		embed = discord.Embed(color = 0xff9900, title = 'Kick')
		embed.add_field(name=f'User *{ user }* kicked from this server successfully. ', value=f'Reason: none', inline=False)
		embed.set_footer(text=f'{ footertext }')
		await ctx.send(embed = embed)
	else:
		await user.kick(reason=reason)
		embed = discord.Embed(color = 0xff9900, title = 'Kick')
		embed.add_field(name=f'User *{ user }* kicked from this server successfully. ', value=f'Reason: { reason }', inline=False)
		embed.set_footer(text=f'{ footertext }')
		await ctx.send(embed = embed)

@bot.command(brief="Purging the channel")
@commands.has_permissions(manage_messages=True)
async def mod_clear(ctx, number: int):
	await ctx.channel.purge(limit=number)
	embed = discord.Embed(color = 0xff9900, title = 'Channel purged sucessfull')
	embed.set_footer(text=f'{ footertext }')
	await ctx.send(embed = embed)

@bot.command(brief="Warns the member")
@commands.has_permissions(kick_members=True)
async def mod_warn(ctx, user: discord.Member, *, reason = None):
	embed = discord.Embed(color = 0xff9900, title = 'Warn')
	embed.add_field(name=f'User *{ user }* warned on this server successfully by *{ ctx.author.name }*. ', value=f'Reason: { reason }', inline=False)
	embed.set_footer(text=f'{ footertext }')
	await ctx.send(embed = embed)

	embed = discord.Embed(color = 0xff9900, title = 'Warn')
	embed.add_field(name=f'Hello *{ user }*! You are got warn on server *{ ctx.guild.name }* by *{ ctx.author.name }*.', value=f'Reason: { reason }', inline=False)
	embed.set_footer(text=f'{ footertext }')
	await user.send(embed = embed)

# DragonBot Debug commands

@bot.command(brief="Bot manager (Only avialable for bot owner)")
@commands.is_owner()
async def db_manage(ctx):
	await ctx.send("Bot management",
		components = [
			Button(label = "Shutdown", custom_id = "Shutdown", style = ButtonStyle.red),
			Button(label = "Restart", custom_id = "Restart", style = ButtonStyle.green),
			Button(label = "Update Status", custom_id = "Update Status", style = ButtonStyle.blue)
		]
	)
	interaction = await bot.wait_for("button_click")
	
	if interaction.custom_id == 'Shutdown':
		embed = discord.Embed(color = 0xff9900, title = 'Bot shutdowning... ' + loadingEmoji)
		embed.set_footer(text=f'{ footertext }')
		await interaction.respond(embed = embed)
		await bot.change_presence(status=discord.Status.idle, activity=discord.Game(f"Shutdowning..."))
		await bot.close()
	if interaction.custom_id == 'Restart':
		embed = discord.Embed(color = 0xff9900, title = 'Bot restarting... ' + loadingEmoji)
		embed.set_footer(text=f'{ footertext }')
		await interaction.respond(embed = embed)
		await bot.change_presence(status=discord.Status.idle, activity=discord.Game(f"Restarting..."))
		os.system('python bot.pyw')
		embed = discord.Embed(color = 0xff9900, title = 'If you see that message bot is not restarted')
		embed.set_footer(text=f'An error occured while restarting the bot')
		await ctx.send(embed = embed)
		await bot.change_presence(status=discord.Status.idle, activity=discord.Game(f"An error occured while restarting the bot"))
		time.sleep(3)
		await bot.change_presence(status=discord.Status.idle, activity=discord.Game(f"db/help | I'm on {len(bot.guilds)} servers"))
	if interaction.custom_id == 'Update Status':
		await bot.change_presence(status=discord.Status.idle, activity=discord.Game(f"{bot_prefix}help | I'm on {len(bot.guilds)} servers"))
		embed = discord.Embed(color = 0xff9900, title = 'Status updated!')
		embed.set_footer(text=f'{ footertext }')
		await interaction.respond(embed=embed)

# Commands for server

# Verification

@bot.command(brief="Verification (Only avialable for bot owner)")
@commands.is_owner()
async def db_verify(ctx, verifyCodeResponse):
	if verifyCodeResponse == '17':
		member = ctx.message.author
		role = get(member.guild.roles, name="Verified Member")
		await member.add_roles(role)
	else:
		await ctx.author.send("You're a bot")
		await ctx.author.kick(reason="You're a bot")

bot.run(bot_token)