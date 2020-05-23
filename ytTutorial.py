import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')
TOKEN = 'TOKEN_Goes_Here'


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
