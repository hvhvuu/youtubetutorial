import discord
from discord.ext import commands

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

client.run(TOKEN)
