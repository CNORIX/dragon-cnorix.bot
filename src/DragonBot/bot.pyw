print('Loading...')

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
import youtube_dl

bot_prefix = 'db/'
bot_token = 'MTAxMTYzODc1Mzg2NzA5MTk3OA.GtuOhE.N57ML0YRKk0opUyevO6FuralG6oHrC6e3aDDmQ'

bad_words = ["bitch", "poop", "dump", "stupid", "тупой", "глупый", "говно", "сука", "пиздец", "хуй", "нахуй", "похуй"]
hi_words = ["hi", "hello"]
how_are_you_words = ["how are you?", "how is it going?"]

activity = discord.Streaming(name=f"{bot_prefix}help", url="https://www.twitch.tv/discord")
bot = commands.Bot(command_prefix = f'{ bot_prefix }', intents=discord.Intents.all(), help_command=None, activity=activity, status=discord.Status.idle)
DiscordComponents(bot)

alwaysOnline = 'No'
footertext = 'DragonBot By DragonFire. Powered by Python'
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
async def on_message( message ):
	data = {"username": f"{message.author.name}", "discriminator": f"{message.author.discriminator}", "userid": f"{message.author.id}"}
	with open(f'messageUsers\\{message.author.name}.json', 'w') as outfile:
		json.dump(data, outfile)

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

# Help Command
@bot.command()
async def help(ctx):
	embed = discord.Embed(color = discord.Colour.from_rgb(156, 0, 0), title = 'Help')
	embed.add_field(name=f'{ bot_prefix }animals', value=f"Showing animals", inline=True)
	embed.add_field(name=f'{ bot_prefix }chnick [ User mention ] [ New Nickname]', value=f'Changing nickname', inline=True)
	embed.add_field(name=f'{ bot_prefix }db_manage', value=f'Bot manager (Only avialable for bot owner)', inline=True)
	embed.add_field(name=f'{ bot_prefix }db_verify', value=f'Verification (Only avialable for bot owner)', inline=True)
	embed.add_field(name=f'{ bot_prefix }leave_bot', value=f'Leave bot (Only avialable for bot owner)', inline=True)
	embed.add_field(name=f'{ bot_prefix }faqAndProblems', value=f'Faq & Problems', inline=True)
	embed.add_field(name=f'{ bot_prefix }fun', value=f'Fun', inline=True)
	embed.add_field(name=f'{ bot_prefix }invite', value=f'Invite bot', inline=True)
	embed.add_field(name=f'{ bot_prefix }mod_ban [ User mention ] [ Reason (Default None) ]', value=f'None', inline=True)
	embed.add_field(name=f'{ bot_prefix }mod_kick [ User mention ] [ Reason (Default None) ]', value=f'None', inline=True)
	embed.add_field(name=f'{ bot_prefix }mod_clear [ Message Count ]', value=f'None', inline=True)
	embed.add_field(name=f'{ bot_prefix }mod_warn [ User mention ] [ Reason (Default None) ]', value=f'None', inline=True)
	embed.add_field(name=f'{ bot_prefix }music_play [ YouTube Video URL ]', value=f'Play music by YouTube URL', inline=True)
	embed.add_field(name=f'{ bot_prefix }music_control', value=f'Music control', inline=True)
	embed.add_field(name=f'{ bot_prefix }tools', value=f'Tools', inline=True)
	embed.add_field(name=f'{ bot_prefix }tools_math', value=f'Simple calculator (Example: "db/tools_math 2 + 2")', inline=True)
	embed.add_field(name=f'{ bot_prefix }tools_ng', value=f'Fing music on Newgrounds (Example: "db/tools_ng 1022162")', inline=True)
	embed.add_field(name=f'{ bot_prefix }tools_reportBug', value=f'Reporting a bug', inline=True)
	embed.add_field(name=f'{ bot_prefix }voice_control', value=f'None', inline=True)
	embed.add_field(name=f'{ bot_prefix }ping', value=f'Shows ping', inline=True)
	embed.set_footer(text=f'{ footertext }')
	await ctx.send(embed = embed)

@bot.command()
async def ping(ctx):
    await ctx.send(f'My ping is {bot.latency * 1000}')

# Animals images
@bot.command(brief = 'Animals')
async def animals(ctx):
	await ctx.send("Animals",
		components = [
			Button(label = "Panda", custom_id = "Panda"),
			Button(label = "Dog", custom_id = "Dog"),
			Button(label = "Cat", custom_id = "Cat"),
			Button(label = "Fox", custom_id = "Fox"),
			Button(label = "Show more", custom_id = "Show more")
			# Button(label = "Red Panda", custom_id = "Red Panda"),
			# Button(label = "Koala", custom_id = "Koala")
		]
	)
	interaction = await bot.wait_for("button_click")
	while True:
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

		if interaction.custom_id == 'Show more':
			await ctx.send("Animals",
				components = [
					Button(label = "Red Panda", custom_id = "Red Panda"),
					Button(label = "Koala", custom_id = "Koala")
				]
			)
			interaction = await bot.wait_for("button_click")
			if interaction.custom_id == 'Red Panda':
				response = requests.get('https://some-random-api.ml/img/red_panda')
				json_data = json.loads(response.text)
		
				embed = discord.Embed(color = 0xff9900, title = 'Random Red Panda')
				embed.set_image(url = json_data['link'])
				embed.set_footer(text=f'{ footertext }')
				await interaction.respond(embed = embed)

			if interaction.custom_id == 'Koala':
				response = requests.get('https://some-random-api.ml/img/koala')
				json_data = json.loads(response.text)
		
				embed = discord.Embed(color = 0xff9900, title = 'Random Koala')
				embed.set_image(url = json_data['link'])
				embed.set_footer(text=f'{ footertext }')
				await interaction.respond(embed = embed)

# Fun Commands

@bot.command(brief = 'fun')
async def fun(ctx):
	await ctx.send("Fun",
		components = [
			Button(label = "Random UUID Key", custom_id = "Random UUID Key"),
			Button(label = "Bot ping", custom_id = "Bot ping"),
			Button(label = "Time", custom_id = "Time")
		]
	)
	interaction = await bot.wait_for("button_click")

	if interaction.custom_id == 'Random UUID Key':
		embed = discord.Embed(color = 0xff9900, title = 'UUID Key Generator')
		embed.add_field(name=f'Key: ', value=f'{ uuid.uuid4() }', inline=False)
		embed.set_footer(text=f'{ footertext }')
		await interaction.respond(embed = embed)
	if interaction.custom_id == 'Bot ping':
		embed = discord.Embed(color = 0xff9900, title = 'Bot ping')
		embed.add_field(name=f'Ping: ', value='{0}ms'.format(round(bot.latency, 1)), inline=False)
		embed.set_footer(text=f'{ footertext }')
		await interaction.respond(embed = embed)
	if interaction.custom_id == 'Time':
		now_date = datetime.datetime.now()
		embed = discord.Embed( title = 'Time', description = f'Time in Yekaterinburg: { now_date }', colour = discord.Color.green(), url = 'https://www.timeserver.ru' )

		embed.set_footer( text = f'{ footertext }')
		embed.set_thumbnail( url = 'https://sun9-35.userapi.com/c200724/v200724757/14f24/BL06miOGVd8.jpg' )

		await interaction.respond( embed = embed )

# Tools

@bot.command()
async def invite(ctx):
	await ctx.author.send('Invite bot: https://discord.com/api/oauth2/authorize?client_id=852183551075811368&permissions=8&redirect_uri=http%3A%2F%2Fdragonfire.7m.pl%2Fdragonbot%2Fbot-added%2F&response_type=code&scope=bot%20identify')

	embed = discord.Embed(color = discord.Colour.from_rgb(156, 0, 0), title = 'Link sended')
	embed.add_field(name=f"I'm sended you in dm link to add bot", value=f'I hope you add the bot to your server', inline=False)
	embed.set_footer(text=f'{ footertext }')
	
	await ctx.send(embed = embed)

@bot.command(brief = 'Tools')
async def tools(ctx):
	await ctx.send("Tools",
		components = [
			Button(label = "About Server", custom_id = "About Server"),
			Button(label = "About bot", custom_id = "About bot"),
			Button(label = "About channel", custom_id = "About channel")
		]
	)
	interaction = await bot.wait_for("button_click")
	
	if interaction.custom_id == 'About Server':
		embed = discord.Embed(color = 0xff9900, title = f'About {ctx.guild.name}')
		embed.add_field(name=f'Name: ', value=f'{ctx.guild.name}', inline=False)
		embed.add_field(name=f'Owner: ', value=f'{ctx.guild.owner}', inline=False)
		embed.add_field(name=f'Guild ID: ', value=f'{ctx.guild.id}', inline=False)
		embed.add_field(name=f'Member Count: ', value=f'{ctx.guild.member_count}', inline=False)
		embed.set_footer(text=f'{ footertext }')
		await interaction.respond(embed = embed)
	if interaction.custom_id == 'About bot':
		embed = discord.Embed(color = 0xff9900, title = f'About DragonBot')
		embed.add_field(name=f'Prefix: ', value=f'{bot_prefix}', inline=False)
		embed.add_field(name=f'Servers count: ', value=f'{len(bot.guilds)}', inline=False)
		embed.add_field(name=f'Developer: ', value=f'**DragonFire#4896**', inline=False)
		embed.add_field(name=f'Always online: ', value=f'{ alwaysOnline }', inline=False)
		embed.set_footer(text=f'{ footertext }')
		await interaction.respond(embed = embed)
	if interaction.custom_id == 'About channel':
		embed = discord.Embed(color = 0xff9900, title = f'About channel')
		embed.add_field(name=f'Name: ', value=f'{ctx.channel.name}', inline=False)
		embed.add_field(name=f'ID: ', value=f'{ctx.channel.id}', inline=False)
		embed.add_field(name=f'Position: ', value=f'{ctx.channel.position}', inline=False)
		embed.add_field(name=f'Slow mode: ', value=f'{ ctx.channel.slowmode_delay } seconds', inline=False)
		embed.add_field(name=f'Channel Category: ', value=f'{ ctx.channel.category }', inline=False)
		embed.add_field(name=f'Description: ', value=f'{ ctx.channel.topic }', inline=False)
		embed.set_footer(text=f'{ footertext }')
		await interaction.respond(embed = embed)

# Report a Bug
@bot.command(brief = 'Reporting a bug')
async def tools_reportBug(ctx, *, bugReport):
    report_channel = bot.get_channel(901739375543607366)

    embedreport = discord.Embed(
        title = f'{ctx.author.name}#{ctx.author.discriminator}',
        description = f'{bugReport}',
        colour = discord.Colour.from_rgb(0, 255, 0)
    )
    await report_channel.send(embed=embedreport)

    embedreportbugsuccess = discord.Embed(
        title = f'Successfully',
        description = f'Your bug report has been sent',
        colour = discord.Colour.from_rgb(0, 255, 0)
    )
    await ctx.send(embed=embedreportbugsuccess)

# Simple calculator
@bot.command(brief = 'Simple calculator (Example: "db/tools_math 2 + 2")')
async def tools_math( ctx, a : int, arg, b : int ):
    if arg == '+':
        await ctx.send( f'Result: { a + b }' )
 
    elif arg == '-':
        await ctx.send( f'Result: { a - b }' )
 
    elif arg == '/':
        await ctx.send( f'Result: { a / b }' )

    elif arg == '*':
        await ctx.send( f'Result: { a * b }' )

@bot.command(brief = 'Fing music on Newgrounds (Example: "db/tools_ng 1022162")')
async def tools_ng( ctx, musicID: str ):
	embed = discord.Embed(color = 0xff9900, title = 'Newgrounds')
	embed.add_field(name=f'The bot seems to have found something', value=f'https://www.newgrounds.com/audio/listen/' + musicID, inline=False)
	embed.set_footer(text=f'{ footertext }')
	await ctx.send(embed = embed) 

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

# Voice commands

@bot.command()
async def voice_control(ctx):
	await ctx.send("Music control",
		components = [
			Button(label = "Join Voice", custom_id = "Join Voice", style = ButtonStyle.red),
			Button(label = "Leave Voice", custom_id = "Leave Voice", style = ButtonStyle.blue)
		]
	)
	interaction = await bot.wait_for("button_click")
	
	if interaction.custom_id == 'Join Voice':
		global voice
		voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
		channel = ctx.message.author.voice.channel

		if voice and voice.is_connected():
			await voice.move_to(channel)
		else:
			voice = await channel.connect()
			embed = discord.Embed(color = 0xff9900, title = 'Bot was connected to the voice channel successfully')
			embed.set_footer(text=f'{ footertext }')
			await interaction.respond(embed = embed)
	if interaction.custom_id == 'Leave Voice':
		voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
		channel = ctx.message.author.voice.channel

		if voice and voice.is_connected():
			await voice.disconnect()
			embed = discord.Embed(color = 0xff9900, title = 'Bot was disconnected to the voice channel successfully')
			embed.set_footer(text=f'{ footertext }')
			await interaction.respond(embed = embed)
		else:
			voice = await channel.disconnect()
			embed = discord.Embed(color = 0xff9900, title = 'Bot was disconnected to the voice channel successfully')
			embed.set_footer(text=f'{ footertext }')
			await interaction.respond(embed = embed)

@bot.command()
async def music_play(ctx, url : str):
    song_there = os.path.isfile(f'musicPlay\\{ ctx.guild.id }.mp3')
 
    try:
        if song_there:
            os.remove(f'musicPlay\\{ ctx.guild.id }.mp3')
            print('[log] Old file deleted')
    except PermissionError:
        print('[log] Failed to delete a file')
 
    await ctx.send('Please wait')
 
    voice = get(bot.voice_clients, guild = ctx.guild)
 
    ydl_opts = {
        'format' : 'bestaudio/best',
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192'
        }],
    }
 
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('[log] Downloading music...')
        ydl.download([url])
 
    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            name = file
            print(f'[log] Renaming file: {file}')
            os.rename(file, f'musicPlay\\{ ctx.guild.id }.mp3')
 
    voice.play(discord.FFmpegPCMAudio(f'{ ctx.guild.id }.mp3'), after = lambda e: print(f'[log] {name}, Music ended playing'))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07
 
    song_name = name.rsplit('-', 2)
    await ctx.send(f'Now music playing: {song_name[0]}')

@bot.command()
async def music_control(ctx):
	await ctx.send("Music control",
		components = [
			Button(label = "Stop Music", custom_id = "Stop Music", style = ButtonStyle.red),
			Button(label = "Music Replay", custom_id = "Music Replay", style = ButtonStyle.blue)
		]
	)
	interaction = await bot.wait_for("button_click")
	
	if interaction.custom_id == 'Stop Music':
		os.system('taskkill /f /im ffmpeg.exe')
		embed = discord.Embed(color = 0xff9900, title = 'Music stopped')
		embed.set_footer(text=f'{ footertext }')
		await interaction.respond(embed = embed)
	if interaction.custom_id == 'Music Replay':
		voice = get(bot.voice_clients, guild = ctx.guild)
		voice.play(discord.FFmpegPCMAudio(f'musicPlay\\{ ctx.guild.id }.mp3'), after = lambda e: print(f'[log] Music ended playing'))
		voice.source = discord.PCMVolumeTransformer(voice.source)
		voice.source.volume = 1
		embed = discord.Embed(color = 0xff9900, title = 'Music replayed')
		embed.set_footer(text=f'{ footertext }')
		await interaction.respond(embed = embed)

@bot.command()
async def faqAndProblems(ctx):
	embed = discord.Embed(color = discord.Colour.from_rgb(156, 0, 0), title = 'Faq And Problems')
	embed.add_field(name=f'Bot does not play music after "db/music_play"', value=f'I know about this problem. At the moment, please use "db/music_control"', inline=False)
	embed.add_field(name=f'The music is fast and slow', value=f"I know about this problem and i don't know how to solve it", inline=False)
	embed.add_field(name=f'Bot lags very much', value=f'If the bot lags a lot, then most likely the problem is the hosting or my computer. Possibly still heavy load on Discord Api (Discord status: https://discordstatus.com)', inline=False)
	embed.set_footer(text=f'{ footertext }')
	await ctx.send(embed = embed)

# DragonBot Debug commands

@bot.command()
@commands.is_owner()
async def leave_bot(ctx):
	embed = discord.Embed(color = discord.Colour.from_rgb(156, 0, 0), title = 'Bot leaved')
	embed.add_field(name=f'Goodbye server!', value=f'Command executed by bot owner', inline=False)
	embed.set_footer(text=f'{ footertext }')
	leave_botpin = await ctx.send(embed = embed)
	await leave_botpin.pin()
	await ctx.guild.leave()

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

# Test commands


@bot.command()
async def register_betaTest(ctx):
	data = {"username": f"{ctx.author.name}", "discriminator": f"{ctx.author.discriminator}", "userid": f"{ctx.author.id}"}
	with open(f'betaTestUsers\\{ctx.author.name}.json', 'w') as outfile:
		json.dump(data, outfile)

	embed = discord.Embed(color = discord.Colour.from_rgb(156, 0, 0), title = 'Your registried!')
	embed.add_field(name=f'Thank you for registring in DragonBot Test programm', value=f'Me send link in dm for DragonBot discord server', inline=False)
	embed.set_footer(text=f'{ footertext }')
	
	await ctx.send(embed = embed)
	await ctx.author.send('https://discord.gg/JTf8ShXceu')

@bot.command()
@commands.is_owner()
async def register_betaTestOwner(ctx, user: discord.Member):
	data = {"username": f"{user.name}", "discriminator": f"{user.discriminator}", "userid": f"{user.id}"}
	with open(f'betaTestUsers\\{user.name}.json', 'w') as outfile:
		json.dump(data, outfile)

	embed = discord.Embed(color = discord.Colour.from_rgb(156, 0, 0), title = 'Your registried!')
	embed.add_field(name=f'Thank you for registring in DragonBot Test programm', value=f'Me send link in dm for DragonBot discord server', inline=False)
	embed.set_footer(text=f'{ footertext }')
	
	await user.send(embed = embed)
	await user.send('https://discord.gg/JTf8ShXceu')

@bot.command()
async def chnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')

# Developers

# Send Request
@bot.command(brief="Send HTTP request. db/sendRequest [url] [get, post]")
@commands.cooldown(1, 30, commands.BucketType.guild)
async def sendRequest(ctx, url, requestType):
	if requestType == 'get':
		getURL = requests.get(url)
		embed = discord.Embed(color = discord.Colour.from_rgb(156, 0, 0), title = 'Requests')
		embed.add_field(name=f'Response code', value=f'```{ getURL }```', inline=False)
		embed.add_field(name=f'HTML Page Parse', value=f'```Sorry, but the parser is not available, because there are a lot of symbols and they do not fit into the embed```', inline=False)
		embed.set_footer(text=f'{ footertext }')
		await ctx.send(embed = embed)
	if requestType == 'post':
		postURL = requests.post(url)
		embed = discord.Embed(color = discord.Colour.from_rgb(156, 0, 0), title = 'Requests')
		embed.add_field(name=f'Response code', value=f'```{ postURL }```', inline=False)
		embed.add_field(name=f'HTML Page Parse', value=f'```Sorry, but the parser is not available, because there are a lot of symbols and they do not fit into the embed```', inline=False)
		embed.set_footer(text=f'{ footertext }')
		await ctx.send(embed = embed)

@bot.command()
async def statuspage(ctx):
	embed = discord.Embed(color = discord.Colour.from_rgb(156, 0, 0), title = 'Statuspage')
	embed.add_field(name=f'URL', value=f'https://dragonfire1.statuspage.io', inline=False)
	embed.set_footer(text=f'{ footertext }')

bot.run(bot_token)
