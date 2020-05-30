import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='!')
TOKEN = 'TOKEN_Goes_here'


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == 'member-log':
            await channel.send(f'Welcome to the server{member.mention}')


@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if str(channel) == 'member-log':
            await channel.send(f'Bye Bye {member.mention}')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    possible_responses = ['That is a resounding no',
            'It is not looking likely',
            'Too hard to tell',
            'It is quite possible',
            'Definitely']
    await ctx.send(random.choice(possible_responses) + ' , ' + ctx.message.author.mention)

client.run(TOKEN)
